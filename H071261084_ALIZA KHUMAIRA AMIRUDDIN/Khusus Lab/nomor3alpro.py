class Produk:
    def __init__(self, kode, nama, harga, stok):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok

class Keranjang:
    def __init__(self):
        self.daftar_produk = {}
        self.checkout_selesai = False

    def tambah(self, produk, jumlah):
        if self.checkout_selesai:
            print("Keranjang sudah checkout")
        elif jumlah <= 0:
            print("Jumlah harus positif")
        else:
            if produk in self.daftar_produk:
                self.daftar_produk[produk] += jumlah
            else:
                self.daftar_produk[produk] = jumlah

    def total(self):
        hasil = 0
        for produk, jumlah in self.daftar_produk.items():
            hasil += produk.harga * jumlah
        return hasil

    def checkout(self):
        if self.checkout_selesai:
            print("Checkout ulang ditolak")
            return

        for produk, jumlah in self.daftar_produk.items():
            if jumlah > produk.stok:
                print("Stok", produk.nama, "tidak mencukupi")
                return

        for produk, jumlah in self.daftar_produk.items():
            produk.stok -= jumlah

        self.checkout_selesai = True
        print("Checkout berhasil")


b = Produk("P01", "Buku", 10000, 5)
p = Produk("P02", "Pena", 5000, 10)

k = Keranjang()

k.tambah(b, 2)
k.tambah(p, 3)

print("Total:", k.total())

k.checkout()

print("Stok buku:", b.stok)
print("Stok pena:", p.stok)