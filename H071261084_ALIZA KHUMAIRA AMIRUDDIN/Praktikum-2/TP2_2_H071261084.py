jarak = int(input("Masukkan jarak pengiriman (km):  "))

if jarak < 0:
    print("Input tidak valid")
else:
    layanan_express = input("Layanan express (Ya/Tidak):  ").capitalize()
    if jarak >= 0 and jarak < 5:
        tarif = 10000
    elif jarak >= 5 and jarak <= 20:
        tarif = 20000
    elif jarak > 20:
        tarif = 35000
    layanan = 15000 if layanan_express == "Ya" else 0
    total_tarif = tarif + layanan 
    print("Total tarif pengiriman:  Rp", total_tarif)