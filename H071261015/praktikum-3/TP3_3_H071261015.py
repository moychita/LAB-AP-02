
while True:
    try:
        N = int(input("masukkan maksimal kursi bus: "))
        if N <= 0:
            print("jumlah kursi harus lebih dari nol")
            continue
        
        break
    except ValueError:
        print("input harus berupa angka")
        
sisa_kursi = N
total_pendapatan = 0


print("--- sistem reservasi PO BUS dimulai ---")

while sisa_kursi >0:
    print(f"sisa kursi: {sisa_kursi}")
    
    try:
        umur = int(input("masukkan umur penupang: "))
        if umur <0:
            print("umur tidak valid")
            continue
                    
        elif umur >=1 and umur <=5:
            harga = 0
            print("Kategori: Balita - Tiket Gratis (Rp 0)")
        
        elif umur >=6 and umur <=12:
            harga = 50000
            print("kategori: anak - harga (Rp 50.000)")
            
        else:
            harga = 100000
            print("kategori: dewasa - harga (Rp 100.000)")
            
        sisa_kursi -= 1
        total_pendapatan += harga
        
    except ValueError:
        print("input harus berupa angka!")
        
print("--- semua kursi terisi ---")
print(f"total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")        
