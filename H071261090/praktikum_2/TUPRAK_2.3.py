nilai = int(input("masukkan nilai tes:" ))
if nilai >= 80 :
    print("lolos ke tahap wawancara")
else :
    pengalaman = int(input("masukan pengalaman kerja (tahun)"))

    if nilai >= 65 and pengalaman >= 2 :
        print("lolos bersyarat")
    else :
        print("tidak lolos")

