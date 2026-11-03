class Buku:
    def __init__(self, kode, judul):
        self.kode = kode
        self.judul = judul
        self.peminjam = None

class Anggota:
    def __init__(self, kode_anggota, nama):
        self.kode_anggota = kode_anggota
        self.nama = nama
        self.daftar_pinjaman = []

    def pinjam(self, buku):
        if buku.peminjam != None:
            print("Buku sudah dipinjam")
        elif len(self.daftar_pinjaman) > 3:
            print("Maksimal 3 buku")
        else:
            buku.peminjam = self
            self.daftar_pinjaman.append(buku)
            print("Buku berhasil dipinjam")

    def kembalikan (self, buku):
        if buku.peminjam != self:
            print("Bukan peminjam buku ini!")
        else:
            buku.peminjam = None
            self.daftar_pinjaman.remove(buku)

b = Buku("B001", "Python Dasar")
a1 = Anggota("A001", "Ayu")
a2 = Anggota("A002", "Bima")
a1.pinjam(b)

print("Peminjam:", b.peminjam.nama)
print("Jumlah pinjaman:", len(a1.daftar_pinjaman))

a2.kembalikan(b)
a1.kembalikan(b)
print("Peminjam sekarang:", b.peminjam)
