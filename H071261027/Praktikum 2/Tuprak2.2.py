jarak = int(input("Masukkan jarak pengiriman (km): "))
if jarak > 0:
    if jarak < 5:
        tarif = 10000
    elif 5<= jarak < 20:
        tarif = 20000
    else:
        tarif = 35000

    layanan = input("Layanan Express (ya/tidak):")
    tarif_tambahan = 15000 if layanan == "ya" else 0
    total_tarif = tarif + tarif_tambahan
    print("Total tarif pengiriman: Rp", total_tarif)
    
else: 
    print("Tidak valid.")