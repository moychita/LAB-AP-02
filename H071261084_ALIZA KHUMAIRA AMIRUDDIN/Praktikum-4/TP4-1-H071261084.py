print("Selamat datang di Kasir Minimarket!")

status_member = str(input("Apakah Anda member? (y/n): "))
def hitungi(harga, jumlah, adalah_member=False):
    subtotal = harga*jumlah
    if adalah_member:
        diskon = subtotal*0.1
        subtotal = subtotal - diskon
    return int(subtotal)
    
if status_member == "y":
     member = True
else:
    member = False

total = 0 
while True:
    nama_barang = str(input("Masukkan nama barang (kosongkan untuk selesai):  "))
    if nama_barang == "":
        break
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang:  "))
    subtotal = hitungi(harga, jumlah, member)
    print(f"Subtotal {nama_barang}: Rp{subtotal}")
    total+= subtotal

print(f"Total belanja: Rp{total}")
