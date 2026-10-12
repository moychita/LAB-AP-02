print("---Rekapitulasi Transaksi Dins Store---")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi.")

while True:

    try:
        jumlah = int(input("masukkan jumlah item:"))
        if jumlah < 0:
            print("Jumlah item tidak boleh negatif")
            continue
        elif jumlah >100:
            print("maksimal 100 item per transaksi!")
            continue
        elif jumlah == 0:
            print("Toko ditutup. Sesi rekap selesai.")
            break     
    except ValueError:
            print("Input harus berupa angka!")
    else:
        print(f"Transaksi {jumlah} berhasil!")
    