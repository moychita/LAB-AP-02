nilai_tes = int(input("Masukkan nilai tes: "))


if 100 >= nilai_tes >= 80:
    print("Lolos ke Tahap Wawancara")  
else:
    pengalaman_kerja = int(input("Masukkan pengalaman kerja (tahun): "))
    if pengalaman_kerja >= 2:
        print("Lolos Bersyarat")
    else:
        print("Tidak Lolos")