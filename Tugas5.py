import numpy as np
import matplotlib.pyplot as plt


class SVMLinearManual:
    def __init__(self):
        self.w = None
        self.b = None
        self.support_vectors_ = None
        self.support_vector_labels_ = None
        self.support_vector_names_ = None

    def fit(self, X, y, names):
        # Pisahkan data kelas positif dan negatif
        pos_idx = np.where(y == 1)[0]
        neg_idx = np.where(y == -1)[0]

        # Cari pasangan titik terdekat dari dua kelas berbeda
        min_distance = float("inf")
        best_pos = None
        best_neg = None

        for i in pos_idx:
            for j in neg_idx:
                distance = np.linalg.norm(X[i] - X[j])

                if distance < min_distance:
                    min_distance = distance
                    best_pos = i
                    best_neg = j

        # Ambil support vector positif dan negatif
        x_pos = X[best_pos]
        x_neg = X[best_neg]

        # Hitung vektor d
        d = x_pos - x_neg

        # Hitung w
        self.w = 2 * d / np.dot(d, d)

        # Hitung b menggunakan support vector positif
        self.b = 1 - np.dot(self.w, x_pos)

        # Simpan support vectors
        self.support_vectors_ = np.array([x_pos, x_neg])
        self.support_vector_labels_ = np.array([y[best_pos], y[best_neg]])
        self.support_vector_names_ = [names[best_pos], names[best_neg]]

        return self

    def decision_function(self, X):
        return np.dot(X, self.w) + self.b

    def predict(self, X):
        return np.sign(self.decision_function(X))

    def margin(self):
        return 2 / np.linalg.norm(self.w)


# Dataset Tugas 1
X = np.array([
    [3, 3],  # A
    [4, 3],  # B
    [1, 1],  # C
    [2, 1]   # D
])

y = np.array([1, 1, -1, -1])
names = np.array(["A", "B", "C", "D"])

# Model SVMLinearManual
model = SVMLinearManual()
model.fit(X, y, names)

# Hasil model
print("Hasil Implementasi SVMLinearManual")
print("w =", model.w)
print("b =", model.b)
print("Support vectors =", model.support_vectors_)
print("Nama support vectors =", model.support_vector_names_)
print("Margin =", model.margin())

# Verifikasi constraint
f_x = model.decision_function(X)
constraint = y * f_x

print("\nVerifikasi Constraint")
for i in range(len(X)):
    print(
        names[i],
        "x =", X[i],
        "y =", y[i],
        "f(x) =", round(f_x[i], 4),
        "y*f(x) =", round(constraint[i], 4)
    )

# Plot decision boundary
x1_range = np.linspace(0, 5, 200)

# Rumus garis:
# w1*x1 + w2*x2 + b = c
def line(c):
    return (c - model.b - model.w[0] * x1_range) / model.w[1]

plt.figure(figsize=(8, 6))

# Plot titik positif dan negatif
plt.scatter(X[y == 1, 0], X[y == 1, 1], marker="o", label="Kelas +1")
plt.scatter(X[y == -1, 0], X[y == -1, 1], marker="x", label="Kelas -1")

# Label titik
for i in range(len(X)):
    plt.text(X[i, 0] + 0.05, X[i, 1] + 0.05, names[i])

# Plot hyperplane dan margin
plt.plot(x1_range, line(0), label="Decision Boundary f(x)=0")
plt.plot(x1_range, line(1), linestyle="--", label="Margin Positif f(x)=1")
plt.plot(x1_range, line(-1), linestyle="--", label="Margin Negatif f(x)=-1")

# Lingkari support vectors
plt.scatter(
    model.support_vectors_[:, 0],
    model.support_vectors_[:, 1],
    s=180,
    facecolors="none",
    edgecolors="black",
    label="Support Vectors"
)

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("SVMLinearManual pada Dataset Tugas 1")
plt.xlim(0, 5)
plt.ylim(0, 4)
plt.grid(True)
plt.legend()
plt.show()