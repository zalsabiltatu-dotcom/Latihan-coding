def hitung_atom():
    print("\n=== Kalkulator Struktur Atom ===")

    # fungsi untuk ubah None jadi "-"
    def tampilkan(nilai):
        return nilai if nilai is not None else "-"

    # inisialisasi semua nilai None
    p = n = e = A = q = None
    rumus = []

    while True:
        print("\nPilih menu untuk memasukkan nilai yang ingin kamu hitung:")
        print("1. Masukkan Proton (p)")
        print("2. Masukkan Neutron (n)")
        print("3. Masukkan Elektron (e)")
        print("4. Masukkan Massa Atom (A)")
        print("5. Masukkan Muatan (q)")
        print("6. Hitung nilai atom")

        pilihan = input("Masukkan nomor menu (1-6): ")

        if pilihan == "1":
            val = input("Masukkan nilai Proton (p): ")
            p = int(val) if val else None
        elif pilihan == "2":
            val = input("Masukkan nilai Neutron (n): ")
            n = int(val) if val else None
        elif pilihan == "3":
            val = input("Masukkan nilai Elektron (e): ")
            e = int(val) if val else None
        elif pilihan == "4":
            val = input("Masukkan nilai Massa Atom (A): ")
            A = int(val) if val else None
        elif pilihan == "5":
            val = input("Masukkan nilai Muatan (q): ")
            q = int(val) if val else None
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid! Silakan pilih menu 1-6.")

    # =========================
    # HITUNG NOMOR MASSA
    # =========================
    if A is None and p is not None and n is not None:
        A = p + n
        rumus.append("A = p + n")
    elif A is not None and p is not None and n is None:
        n = A - p
        rumus.append("n = A - p")
    elif A is not None and n is not None and p is None:
        p = A - n
        rumus.append("p = A - n")

    # =========================
    # HITUNG MUATAN / ELEKTRON
    # =========================
    if q is None and p is not None and e is not None:
        q = p - e
        rumus.append("q = p - e")
    elif q is not None and p is not None and e is None:
        e = p - q
        rumus.append("e = p - q")
    elif q is not None and e is not None and p is None:
        p = q + e
        rumus.append("p = q + e")

    # =========================
    # TENTUKAN JENIS ATOM / ION
    # =========================
    jenis = "Tidak diketahui"
    if p is not None and e is not None:
        if p == e:
            jenis = "Atom netral"
        elif p > e:
            jenis = f"Kation (muatan +{p - e})"
        else:
            jenis = f"Anion (muatan {p - e})"

    # =========================
    # MENENTUKAN JENIS UNSUR (1–20)
    # =========================
    unsur = "Tidak diketahui"

    tabel_unsur = {
        1: "Hidrogen (H)",
        2: "Helium (He)",
        3: "Litium (Li)",
        4: "Berilium (Be)",
        5: "Boron (B)",
        6: "Karbon (C)",
        7: "Nitrogen (N)",
        8: "Oksigen (O)",
        9: "Fluorin (F)",
        10: "Neon (Ne)",
        11: "Natrium (Na)",
        12: "Magnesium (Mg)",
        13: "Aluminium (Al)",
        14: "Silikon (Si)",
        15: "Fosfor (P)",
        16: "Sulfur (S)",
        17: "Klorin (Cl)",
        18: "Argon (Ar)",
        19: "Kalium (K)",
        20: "Kalsium (Ca)"
    }

    if p in tabel_unsur:
        unsur = tabel_unsur[p]

    # =========================
    # OUTPUT
    # =========================
    print("\n=== Hasil Perhitungan ===")
    print(f"Proton (p): {tampilkan(p)}")
    print(f"Neutron (n): {tampilkan(n)}")
    print(f"Elektron (e): {tampilkan(e)}")
    print(f"Massa Atom (A): {tampilkan(A)}")
    print(f"Muatan (q): {tampilkan(q)}")
    print(f"Jenis Atom/Ion: {jenis}")
    print(f"Jenis Unsur: {unsur}")

    # tampilkan rumus yang digunakan
    if rumus:
        print("\nRumus yang digunakan:")
        for r in rumus:
            print(r)
    else:
        print("\nTidak ada rumus yang perlu digunakan, input sudah lengkap.")


# =========================
# Jalankan program
# =========================
if __name__ == "__main__":
    while True:
        hitung_atom()
        lagi = input("\nIngin menghitung atom lain? (y/n): ").lower()
        if lagi != "y":
            print("Terima kasih telah menggunakan kalkulator atom!")
            break