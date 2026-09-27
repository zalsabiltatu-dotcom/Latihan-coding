# Inisialisasi variabel dan parameter
x = 0.0  # Tebakan awal
y = 0.0  # Tebakan awal
jumlah_iterasi = 10

print("\nHasil Iterasi Metode Gauss-Seidel:")
print("Iterasi |   x   |   y")
print("-" * 28)

for i in range(1, jumlah_iterasi + 1):
    # Menghitung x baru dan langsung memperbarui nilai x
    x = (5 - y) / 4

    # Menghitung y baru menggunakan nilai x yang sudah diperbarui
    y = (7 - x) / 3

    print(f"{i:2d} | {x:.5f} | {y:.5f}")