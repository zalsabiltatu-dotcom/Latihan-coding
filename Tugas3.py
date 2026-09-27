import zipfile
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


# =========================================
# TUGAS 3: ANALISIS PENGARUH NILAI K
# Dataset: citrus.csv
# =========================================


# 1. Ekstrak dan baca dataset
# Pastikan file zip berada satu folder dengan file Python ini.
zip_path = "archive (1)(3).zip"
extract_dir = "archive_extracted"

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(extract_dir)

csv_path = os.path.join(extract_dir, "citrus.csv")
data = pd.read_csv(csv_path)

print("Jumlah data asli:", len(data))
print(data.head())


# 2. Membuat subset data seimbang
orange_data = data[data["name"] == "orange"].sample(n=500, random_state=42)
grapefruit_data = data[data["name"] == "grapefruit"].sample(n=500, random_state=42)

subset = pd.concat([orange_data, grapefruit_data], axis=0)
subset = subset.sample(frac=1, random_state=42).reset_index(drop=True)

print("\nJumlah subset:")
print(subset["name"].value_counts())


# 3. Mengambil fitur dan label
X = subset[["weight", "diameter"]].values
y = subset["name"].values


# 4. Split manual 80% data latih dan 20% data uji
np.random.seed(42)

indices = np.arange(len(X))
np.random.shuffle(indices)

split_index = int(0.8 * len(X))

train_idx = indices[:split_index]
test_idx = indices[split_index:]

X_train = X[train_idx]
y_train = y[train_idx]

X_test = X[test_idx]
y_test = y[test_idx]

print("\nJumlah data latih:", len(X_train))
print("Jumlah data uji:", len(X_test))


# 5. Membuat class KNN manual
class KNNManual:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X_train, y_train):
        self.X_train = np.array(X_train, dtype=float)
        self.y_train = np.array(y_train)

    def euclidean_distance(self, p, q):
        diff = p - q
        return np.sqrt(np.dot(diff, diff))

    def predict_one(self, x_test):
        distances = []

        for i, x_train in enumerate(self.X_train):
            d = self.euclidean_distance(x_test, x_train)
            distances.append((d, self.y_train[i], i + 1))

        distances.sort(key=lambda x: x[0])

        k_neighbors = distances[:self.k]
        k_labels = [label for distance, label, index in k_neighbors]

        most_common = Counter(k_labels).most_common(1)
        return most_common[0][0]

    def predict(self, X_test):
        predictions = []

        for x in X_test:
            pred = self.predict_one(x)
            predictions.append(pred)

        return np.array(predictions)

    def distance_table(self, x_test, top_n=9):
        rows = []

        for i, x_train in enumerate(self.X_train):
            d = self.euclidean_distance(np.array(x_test, dtype=float), x_train)
            rows.append((i + 1, x_train[0], x_train[1], self.y_train[i], d))

        rows.sort(key=lambda x: x[4])
        return rows[:top_n]


# 6. Accuracy score manual
def accuracy_score_manual(y_true, y_pred):
    benar = 0

    for actual, pred in zip(y_true, y_pred):
        if actual == pred:
            benar += 1

    return benar / len(y_true)


# 7. Uji nilai K
k_values = [1, 3, 5, 7, 9]
accuracies = []
correct_counts = []

print("\nHASIL ANALISIS NILAI K")
print("======================")

for k in k_values:
    knn = KNNManual(k=k)
    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)

    acc = accuracy_score_manual(y_test, y_pred)
    benar = np.sum(y_test == y_pred)

    accuracies.append(acc)
    correct_counts.append(benar)

    print("\nK =", k)
    print("Prediksi benar:", benar, "dari", len(y_test))
    print("Akurasi:", round(acc * 100, 2), "%")


# 8. Tabel akurasi
print("\nTABEL AKURASI")
print("K | Benar | Total Uji | Akurasi")

for k, benar, acc in zip(k_values, correct_counts, accuracies):
    print(f"{k} | {benar} | {len(y_test)} | {acc * 100:.2f}%")


# 9. Tabel jarak 9 tetangga terdekat
knn_9 = KNNManual(k=9)
knn_9.fit(X_train, y_train)

print("\nTABEL JARAK 9 TETANGGA TERDEKAT")

for i in range(5):
    print(f"\nData uji {i + 1}")
    print("Fitur:", X_test[i])
    print("Kelas aktual:", y_test[i])
    print("Rank | Data Latih | Weight | Diameter | Kelas | Jarak")

    rows = knn_9.distance_table(X_test[i], top_n=9)

    for rank, row in enumerate(rows, start=1):
        no_latih, weight, diameter, kelas, jarak = row
        print(f"{rank:>4} | L{no_latih:<9} | {weight:>7.2f} | {diameter:>8.2f} | {kelas:<10} | {jarak:>6.2f}")


# 10. Grafik akurasi terhadap nilai K
plt.figure(figsize=(7, 5))
plt.plot(k_values, [a * 100 for a in accuracies], marker="o")
plt.title("Grafik Akurasi terhadap Nilai K")
plt.xlabel("Nilai K")
plt.ylabel("Akurasi (%)")
plt.xticks(k_values)
plt.grid(True)
plt.savefig("grafik_akurasi_knn_citrus.png", dpi=300, bbox_inches="tight")
plt.show()