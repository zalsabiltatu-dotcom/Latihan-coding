import numpy as np
from collections import Counter


class KNNManual:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X_train, y_train):
        # Menyimpan data latih
        self.X_train = np.array(X_train, dtype=float)
        self.y_train = np.array(y_train)

    def euclidean_distance(self, p, q):
        # Rumus Euclidean:
        # d = sqrt((x1 - y1)^2 + (x2 - y2)^2)
        diff = p - q
        return np.sqrt(np.dot(diff, diff))

    def predict_one(self, x_test):
        # Menghitung jarak data uji ke semua data latih
        distances = []

        for i, x_train in enumerate(self.X_train):
            d = self.euclidean_distance(x_test, x_train)
            distances.append((d, self.y_train[i], i))

        # Mengurutkan jarak dari yang terkecil
        distances.sort(key=lambda x: x[0])

        # Mengambil K tetangga terdekat
        k_neighbors = distances[:self.k]
        k_labels = [label for _, label, _ in k_neighbors]

        # Majority voting
        most_common = Counter(k_labels).most_common(1)
        return most_common[0][0]

    def predict(self, X_test):
        X_test = np.array(X_test, dtype=float)
        return np.array([self.predict_one(x) for x in X_test])

    def distance_table(self, x_test):
        rows = []

        for i, x_train in enumerate(self.X_train):
            d = self.euclidean_distance(np.array(x_test, dtype=float), x_train)
            rows.append((i + 1, x_train[0], x_train[1], self.y_train[i], d))

        rows.sort(key=lambda x: x[4])
        return rows


def accuracy_score_manual(y_true, y_pred):
    benar = 0

    for actual, pred in zip(y_true, y_pred):
        if actual == pred:
            benar += 1

    return benar / len(y_true)


def confusion_matrix_manual(y_true, y_pred, labels):
    matrix = np.zeros((len(labels), len(labels)), dtype=int)
    label_index = {label: i for i, label in enumerate(labels)}

    for actual, pred in zip(y_true, y_pred):
        baris = label_index[actual]
        kolom = label_index[pred]
        matrix[baris][kolom] += 1

    return matrix


# Dataset buah diperluas
# Total data = 25
# Fitur = Berat dan Diameter
X = np.array([
    [150, 8],
    [160, 9],
    [170, 10],
    [155, 8.5],
    [165, 9.5],
    [172, 10.2],
    [145, 7.5],
    [158, 8.8],
    [168, 9.8],
    [152, 8.2],

    [200, 20],
    [220, 22],
    [210, 21],
    [230, 23],
    [205, 19],
    [215, 20.5],
    [225, 22.5],
    [235, 23.5],

    [80, 15],
    [90, 17],
    [75, 14],
    [85, 16],
    [95, 18],
    [100, 17],
    [88, 15.5]
], dtype=float)

y = np.array([
    'Apel', 'Apel', 'Apel', 'Apel', 'Apel',
    'Apel', 'Apel', 'Apel', 'Apel', 'Apel',

    'Mangga', 'Mangga', 'Mangga', 'Mangga',
    'Mangga', 'Mangga', 'Mangga', 'Mangga',

    'Jeruk', 'Jeruk', 'Jeruk', 'Jeruk',
    'Jeruk', 'Jeruk', 'Jeruk'
])


# Split manual 80% data latih dan 20% data uji
# Total 25 data
# Data latih = 20
# Data uji = 5
test_indices = [1, 5, 12, 21, 24]

X_train = np.array([X[i] for i in range(len(X)) if i not in test_indices])
y_train = np.array([y[i] for i in range(len(y)) if i not in test_indices])

X_test = np.array([X[i] for i in test_indices])
y_test = np.array([y[i] for i in test_indices])


# Membuat model KNN
knn = KNNManual(k=3)

# Melatih model
knn.fit(X_train, y_train)

# Melakukan prediksi
y_pred = knn.predict(X_test)


print("HASIL PREDIKSI")
for i in range(len(X_test)):
    print(f"Data uji {i + 1}: X={X_test[i]}, Aktual={y_test[i]}, Prediksi={y_pred[i]}")


# Menghitung akurasi manual
akurasi = accuracy_score_manual(y_test, y_pred)

print("\nAKURASI")
print("Akurasi:", akurasi)
print("Akurasi dalam persen:", akurasi * 100, "%")


# Membuat confusion matrix manual
labels = ['Apel', 'Mangga', 'Jeruk']
cm = confusion_matrix_manual(y_test, y_pred, labels)

print("\nCONFUSION MATRIX")
print("Baris = Aktual")
print("Kolom = Prediksi")
print("Labels:", labels)
print(cm)


# Menampilkan tabel jarak manual
print("\nTABEL JARAK")

for i, x_uji in enumerate(X_test):
    print(f"\nData uji {i + 1}: {x_uji}, aktual: {y_test[i]}")
    print("Rank | Data Latih | Berat | Diameter | Kelas | Jarak")

    rows = knn.distance_table(x_uji)

    for rank, row in enumerate(rows, start=1):
        no_latih, berat, diameter, kelas, jarak = row
        print(f"{rank:>4} | L{no_latih:<10} | {berat:>5.1f} | {diameter:>8.1f} | {kelas:<6} | {jarak:>6.2f}")

    print("3 tetangga terdekat:")

    for row in rows[:3]:
        no_latih, berat, diameter, kelas, jarak = row
        print(f"L{no_latih}, kelas {kelas}, jarak {jarak:.2f}")