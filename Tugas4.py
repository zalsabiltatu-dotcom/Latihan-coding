import numpy as np
import matplotlib.pyplot as plt

# Dataset
X = np.array([
    [3, 3],  # A
    [4, 3],  # B
    [1, 1],  # C
    [2, 1]   # D
])

y = np.array([1, 1, -1, -1])
nama_titik = ["A", "B", "C", "D"]

# Hyperplane hasil perhitungan manual
w = np.array([0.4, 0.8])
b = -2.6

# Hitung f(x) dan constraint
f = X @ w + b
constraint = y * f

print("w =", w)
print("b =", b)
print()

print("Hasil verifikasi constraint:")
for i in range(len(X)):
    status = "Support Vector" if abs(constraint[i] - 1) < 1e-9 else "Bukan Support Vector"
    print(
        nama_titik[i],
        "x =", X[i],
        "y =", y[i],
        "f(x) =", round(f[i], 2),
        "y*f(x) =", round(constraint[i], 2),
        status
    )

# Hitung margin
norm_w = np.linalg.norm(w)
margin_satu_sisi = 1 / norm_w
margin_total = 2 / norm_w

print()
print("||w|| =", round(norm_w, 4))
print("Margin satu sisi =", round(margin_satu_sisi, 4))
print("Margin total =", round(margin_total, 4))

# Fungsi garis untuk hyperplane dan margin
x1_line = np.linspace(0, 5, 200)

def garis(c):
    # w1*x1 + w2*x2 + b = c
    return (c - b - w[0] * x1_line) / w[1]

# Plot data
plt.figure(figsize=(7, 5))

plt.scatter(X[y == 1, 0], X[y == 1, 1], marker="o", label="Label +1")
plt.scatter(X[y == -1, 0], X[y == -1, 1], marker="x", label="Label -1")

# Label titik
for i in range(len(X)):
    plt.text(X[i, 0] + 0.05, X[i, 1] + 0.05, nama_titik[i])

# Garis hyperplane dan margin
plt.plot(x1_line, garis(0), label="Hyperplane f(x)=0")
plt.plot(x1_line, garis(1), linestyle="--", label="Margin positif f(x)=1")
plt.plot(x1_line, garis(-1), linestyle="--", label="Margin negatif f(x)=-1")

# Penanda support vector
plt.text(3.05, 3.15, "SV A")
plt.text(2.05, 1.15, "SV D")

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Visualisasi Hyperplane SVM Manual")
plt.xlim(0, 5)
plt.ylim(0, 4)
plt.grid(True)
plt.legend()
plt.show()