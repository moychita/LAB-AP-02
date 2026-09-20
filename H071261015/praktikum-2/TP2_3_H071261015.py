
nilai = int(input("Masukkan nilai tes (0-100): "))


if nilai < 0 or nilai > 100:
    print("Nilai tes harus berada antara 0 sampai 100.")
elif nilai >= 80:
            print("Lolos ke Tahap Wawancara")
else:
    pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))

    if pengalaman < 0:
        print("Pengalaman kerja tidak boleh negatif.")
    else:
        if nilai >= 65 and pengalaman >= 2:
            print("Lolos Bersyarat")
        else:
            print("Tidak Lolos")
