print("--- Rekapitulasi Transaksi Dins Store ---")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi.")

while True:
    try:
        jumlah = int(input("Masukkan jumlah item: "))
        
        if jumlah == 0:
            print("toko ditutup. sesi rekap selesai")
            break

        elif jumlah < 0:
            print("jumlah tida boleh negatif")
            continue
        
        elif jumlah > 100:
            print("maksimal 100 item per transaksi!")
            continue
        
        else:
            print(f"transaksi {jumlah} item berhasil!")
        
    except ValueError:
        print("input harus berupa angka!")


