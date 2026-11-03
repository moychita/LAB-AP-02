jarak = int(input("Masukan jarak pengiriman (km):"))

if jarak < 0:
    print("tidak valid")
else:
    express = input("layanan express (ya/tidak):").lower()

    if jarak < 5:
       tarif = 10000
    elif jarak < 20:
       tarif = 20000
    else:
       tarif = 35000

    layanan = 15000 if express == "ya" else 0
    tarif_akhir = tarif + layanan 

    print("total tarif pengirimam:", tarif_akhir)
