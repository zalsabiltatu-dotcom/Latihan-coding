# Inisialisasi variabel dan parameter
x = 0.0      # tebakan awal x
y = 0.0      # tebakan awal y
jumlah_iterasi = 10

print("Hasil Iterasi Metode Jacobi:")
print("Iterasi |   x   |   y")
print("-" * 28)

for i in range(1, jumlah_iterasi + 1):
    # Menghitung nilai baru dengan merujuk pada nilai lama (x dan y)
    x_baru = (5 - y) / 4
    y_baru = (7 - x) / 3

    # Melakukan pembaruan nilai secara serempak
    x = x_baru
    y = y_baru

    print(f"{i:2d} | {x:.5f} | {y:.5f}")