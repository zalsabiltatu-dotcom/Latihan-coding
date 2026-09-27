import math

data = [
    [1, 86.76, 2.96, "orange"],
    [2, 129.25, 6.88, "orange"],
    [3, 137.24, 7.44, "orange"],
    [4, 142.88, 7.83, "orange"],
    [5, 148.14, 8.16, "orange"],
    [6, 152.67, 8.47, "orange"],
    [7, 157.35, 8.79, "orange"],
    [8, 162.52, 9.11, "orange"],
    [9, 168.93, 9.52, "orange"],
    [10, 176.92, 10.07, "orange"],
    [11, 126.79, 7.63, "grapefruit"],
    [12, 172.64, 9.88, "grapefruit"],
    [13, 180.96, 10.44, "grapefruit"],
    [14, 187.39, 10.83, "grapefruit"],
    [15, 192.52, 11.14, "grapefruit"],
    [16, 197.43, 11.45, "grapefruit"],
    [17, 202.55, 11.77, "grapefruit"],
    [18, 207.40, 12.12, "grapefruit"],
    [19, 213.50, 12.53, "grapefruit"],
    [20, 221.85, 13.08, "grapefruit"]
]

def hitung_jarak(berat_uji, diameter_uji, berat_data, diameter_data):
    delta_berat = berat_uji - berat_data
    delta_diameter = diameter_uji - diameter_data

    delta_berat_kuadrat = delta_berat ** 2
    delta_diameter_kuadrat = delta_diameter ** 2

    total = delta_berat_kuadrat + delta_diameter_kuadrat
    jarak = math.sqrt(total)

    return delta_berat, delta_diameter, delta_berat_kuadrat, delta_diameter_kuadrat, total, jarak

def buat_tabel_jarak(data_uji):
    berat_uji = data_uji[0]
    diameter_uji = data_uji[1]

    hasil = []

    for item in data:
        no = item[0]
        berat = item[1]
        diameter = item[2]
        kelas = item[3]

        delta_berat, delta_diameter, delta_berat_kuadrat, delta_diameter_kuadrat, total, jarak = hitung_jarak(
            berat_uji,
            diameter_uji,
            berat,
            diameter
        )

        hasil.append([
            no,
            berat,
            diameter,
            kelas,
            delta_berat,
            delta_diameter,
            delta_berat_kuadrat,
            delta_diameter_kuadrat,
            total,
            jarak
        ])

    return hasil

def tampilkan_tabel_jarak(tabel):
    print("No | Berat | Diameter | Kelas | Δ Berat | Δ Diameter | Δ Berat² | Δ Diameter² | Total | Jarak")
    print("-" * 105)

    for row in tabel:
        print(
            f"{row[0]:2} | "
            f"{row[1]:6.2f} | "
            f"{row[2]:8.2f} | "
            f"{row[3]:10} | "
            f"{row[4]:8.2f} | "
            f"{row[5]:10.2f} | "
            f"{row[6]:9.2f} | "
            f"{row[7]:11.2f} | "
            f"{row[8]:8.2f} | "
            f"{row[9]:6.2f}"
        )

def prediksi_knn(tabel_jarak, k):
    # Urutkan berdasarkan jarak paling kecil
    tabel_urut = sorted(tabel_jarak, key=lambda x: x[9])

    # Ambil sebanyak K tetangga terdekat
    tetangga = tabel_urut[:k]

    # Hitung voting kelas
    suara = {}

    for item in tetangga:
        kelas = item[3]

        if kelas not in suara:
            suara[kelas] = 0

        suara[kelas] += 1

    # Ambil kelas dengan suara terbanyak
    prediksi = max(suara, key=suara.get)

    return prediksi, tetangga, suara

def tampilkan_tetangga(tetangga):
    print("Urutan | No Data | Kelas | Jarak")
    print("-" * 35)

    urutan = 1

    for item in tetangga:
        print(f"{urutan:6} | {item[0]:7} | {item[3]:10} | {item[9]:.2f}")
        urutan += 1

# Data uji
x_test1 = [210, 21]
x_test2 = [85, 16]

# ===============================
# Perhitungan untuk x_test1
# ===============================

print("\nTABEL JARAK x_test1 = (210, 21)")
tabel_x_test1 = buat_tabel_jarak(x_test1)
tampilkan_tabel_jarak(tabel_x_test1)

print("\nPrediksi x_test1 dengan K = 3")
prediksi_1_k3, tetangga_1_k3, suara_1_k3 = prediksi_knn(tabel_x_test1, 3)
tampilkan_tetangga(tetangga_1_k3)
print("Jumlah suara:", suara_1_k3)
print("Hasil prediksi:", prediksi_1_k3)

print("\nPrediksi x_test1 dengan K = 5")
prediksi_1_k5, tetangga_1_k5, suara_1_k5 = prediksi_knn(tabel_x_test1, 5)
tampilkan_tetangga(tetangga_1_k5)
print("Jumlah suara:", suara_1_k5)
print("Hasil prediksi:", prediksi_1_k5)

# ===============================
# Perhitungan untuk x_test2
# ===============================

print("\nTABEL JARAK x_test2 = (85, 16)")
tabel_x_test2 = buat_tabel_jarak(x_test2)
tampilkan_tabel_jarak(tabel_x_test2)

print("\nPrediksi x_test2 dengan K = 3")
prediksi_2_k3, tetangga_2_k3, suara_2_k3 = prediksi_knn(tabel_x_test2, 3)
tampilkan_tetangga(tetangga_2_k3)
print("Jumlah suara:", suara_2_k3)
print("Hasil prediksi:", prediksi_2_k3)