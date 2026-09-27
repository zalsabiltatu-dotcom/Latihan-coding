import numpy as np
A = np.array([
    [10,15,25],
    [12,20,30],
    [5,8,10]
], dtype=float)

b = np.array([900,1100,450], dtype=float)

n = len(b)
# Eliminasi Gauss
for i in range(n):

    for j in range(i+1,n):

        ratio = A[j][i] / A[i][i]

        for k in range(n):
            A[j][k] = A[j][k] - ratio * A[i][k]

        b[j] = b[j] - ratio * b[i]

# Substitusi Mundur
x = np.zeros(n)

x[n-1] = b[n-1] / A[n-1][n-1]

for i in range(n-2,-1,-1):
    sum = 0
    for j in range(i+1,n):
        sum = sum + A[i][j] * x[j]

    x[i] = (b[i] - sum) / A[i][i]

print("Hasil Eliminasi Gauss")
print("CCTV =", x[0])
print("WiFi =", x[1])
print("E-Gov =", x[2])
