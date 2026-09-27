import numpy as np

# Luas awal
luas_awal = 120

# Matriks transformasi
M = np.array([
    [3, 0],
    [0, 2]
])

# Menghitung determinan matriks
determinan = np.linalg.det(M)

# Luas setelah transformasi = |determinan| × luas_awal
luas_akhir = abs(determinan) * luas_awal

print(f"Matriks transformasi:")
print(M)
print(f"\nDeterminan matriks = {determinan:.0f}")
print(f"Luas awal = {luas_awal} m²")
print(f"Luas setelah transformasi = |{determinan:.0f}| × {luas_awal} = {luas_akhir:.0f} m²")
    