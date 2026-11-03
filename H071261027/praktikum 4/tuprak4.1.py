print("Selamat datang di Kasir Minimarket!")
status_member = input("Apakah Anda member? (y/n): ")
member = status_member.lower() == "y"
def hitung_subtotal(harga, jumlah, member):
    if member:
        return harga * jumlah * 0.9
    else:
        return harga * jumlah

total = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if nama_barang == "":
        break 
    harga = int(input("Masukkan harga barang: "))
    jumlah = int(input("Masukkan jumlah barang: "))
    subtotal = hitung_subtotal(harga, jumlah, member)  
    print(f"Subtotal {nama_barang}: Rp{subtotal}")
    total += subtotal
print(f"Total: Rp{total}")