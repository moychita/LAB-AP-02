jarak = int(input("Masukkan jarak pengiriman (KM): "))
layanan_express = input("Apakah anda ingin menggunakan layanan express? (ya/tidak): ").lower()

if 0 < jarak < 5:
    biaya = 10000
elif 5 <= jarak <= 20:
    biaya = 20000
elif jarak > 20:
    biaya = 35000
else:  
    print("Jarak tidak valid")

layanan = 15000 if layanan_express == "ya" else 0
tarif_total = biaya + layanan
print("Total tarif pengiriman : Rp", tarif_total)