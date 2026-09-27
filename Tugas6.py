import numpy as np


class SVMLinearManual:
    def __init__(self, lr=0.001, lambda_param=0.01, C=1.0, epochs=5000):
        self.lr = lr
        self.lambda_param = lambda_param
        self.C = C
        self.epochs = epochs
        self.w = None
        self.b = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # Konversi label ke -1 dan +1
        y_ = np.where(y <= 0, -1, 1)

        self.w = np.zeros(n_features)
        self.b = 0

        for epoch in range(self.epochs):
            for i, x_i in enumerate(X):
                condition = y_[i] * (np.dot(x_i, self.w) + self.b) >= 1

                if condition:
                    # Jika sudah benar dan di luar margin
                    self.w -= self.lr * (2 * self.lambda_param * self.w)
                else:
                    # Jika salah klasifikasi atau masuk area margin
                    self.w -= self.lr * (
                        2 * self.lambda_param * self.w
                        - self.C * y_[i] * x_i
                    )
                    self.b += self.lr * self.C * y_[i]

    def predict(self, X):
        approx = np.dot(X, self.w) + self.b
        return np.sign(approx)

    def decision_function(self, X):
        return np.dot(X, self.w) + self.b

    def margin(self):
        norm_w = np.linalg.norm(self.w)
        return 2.0 / norm_w if norm_w > 0 else float("inf")

    def functional_margin(self, X, y):
        y_ = np.where(y <= 0, -1, 1)
        return y_ * self.decision_function(X)

    def support_vectors(self, X, y):
        margins = self.functional_margin(X, y)
        return np.where(margins <= 1)[0]


# ==========================
# Dataset dengan outlier
# ==========================
X = np.array([
    [1, 1],
    [2, 2],
    [2, 0],
    [0, 0],
    [1, 0],
    [0, 1],
    [0.2, 0.2]   # outlier
], dtype=float)

y = np.array([1, 1, 1, -1, -1, -1, 1])


# ==========================
# Eksperimen nilai C
# ==========================
nilai_C = [0.1, 1, 10, 100]

for C in nilai_C:
    svm = SVMLinearManual(
        lr=0.001,
        lambda_param=0.01,
        C=C,
        epochs=5000
    )

    svm.fit(X, y)

    prediksi = svm.predict(X)
    akurasi = np.mean(prediksi == y)
    functional_margins = svm.functional_margin(X, y)
    sv_index = svm.support_vectors(X, y)

    print("====================================")
    print("Nilai C           :", C)
    print("Vektor bobot w    :", svm.w)
    print("Bias b            :", svm.b)
    print("Lebar margin      :", svm.margin())
    print("Prediksi          :", prediksi)
    print("Aktual            :", y)
    print("Akurasi           :", akurasi)
    print("Functional margin :", functional_margins)
    print("Index support vector:", sv_index)
    print("Jumlah support vector:", len(sv_index))