# class Hewan:
#     def __init__(self, nama):
#         self.nama = nama

#     def bersuara(self):
#         return "..."

# class Kucing(Hewan):
#     def bersuara(self):
#         return "Meong"

#     def mencakar(self):
#         return f"{self.nama} mencakar!"

# k = Kucing("Tom")
# print(k.bersuara())
# print(k.mencakar())

# class Karyawan:
#     def __init__(self, nama, gaji):
#         self.nama = nama
#         self.gaji = gaji

#     def info(self):
#         return f"{self.nama} - Rp{self.gaji}" 

# class Manajer(Karyawan):
#     def __init__(self, nama, gaji, tim):
#         super().__init__(nama, gaji)
#         self.tim = tim

#     def info(self):
#         return super().info() + f" | Tim: {self.tim}"

# m = Manajer("Sari", 15000000, "MRE")
# print(m.info())

# class Terbang:
#     def gerak(self):
#         return "terbang"

# class Berenang:
#     def gerak(self):
#         return "berenang"

# class Bebek(Terbang, Berenang):
#     pass

# b = Bebek()
# print(b.gerak())
# print((c.__name__ for c in Bebek.__mro__))


# class Rekening:
#     def __init__(self, pemilik, saldo=0):
#         self.pemilik = pemilik
#         self.saldo = saldo

#     def tarik(self, jumlah):
#         if jumlah > self.saldo:
#             return "Saldo tidak cukup"
#         self.saldo -= jumlah
#         return f"Sisa saldo: {self.saldo}"

# class Tabungan(Rekening):
#     def __init__(self, pemilik, saldo, bunga):
#         super().__init__(pemilik, saldo)
#         self.bunga = bunga

#     def tambah_bunga(self):
#         self.saldo += self.saldo * self.bunga

# class Giro(Rekening):
#     def tarik(self, jumlah): 
#         if jumlah > self.saldo + 500000:
#             return "Melebihi batas"
#         self.saldo -= jumlah
#         return f"Sisa saldo: {self.saldo}"

# t = Tabungan("Ani", 1000000, 0.02)
# t.tambah_bunga()
# print(t.saldo)

# g = Giro("Budi", 100000)
# print(g.tarik(400000))


# class BangunDatar:
#     def luas(self):
#         return 0
#     def keliling(self):
#         return 0

# class Persegi(BangunDatar):
#     def __init__(self, sisi):
#         self.sisi = sisi

#     def luas(self):
#         return self.sisi * self.sisi

#     def keliling(self):
#         return 4 * self.sisi

# class Lingkaran(BangunDatar):
#     def __init__(self, r):
#         self.r = r

#     def luas(self):
#         return 3.14 * self.r * self.r

#     def keliling(self):
#         return 2 * 3.14 * self.r

# daftar_bangun = [Persegi(5), Lingkaran(7)]

# print("Luas Persegi:", daftar_bangun[0].luas())
# print("Keliling Persegi:", daftar_bangun[0].keliling())
# print("Luas Lingkaran:", daftar_bangun[1].luas())
# print("Keliling Lingkaran:", daftar_bangun[1].keliling())


# class BangunDatar:
#     def luas(self):
#         return 0
#     def keliling(self):
#         return 0

# class Persegi(BangunDatar):
#     def __init__(self, sisi):
#         self.sisi = sisi
#     def luas(self):
#         return self.sisi * self.sisi
#     def keliling(self):
#         return 4 * self.sisi

# class Lingkaran(BangunDatar):
#     def __init__(self, r):
#         self.r = r
#     def luas(self):
#         return 3.14 * self.r * self.r
#     def keliling(self):
#         return 2 * 3.14 * self.r

# daftar_bangun = [Persegi(5), Lingkaran(7)]
# print("Luas Persegi:", daftar_bangun[0].luas())
# print("Keliling Persegi:", daftar_bangun[0].keliling())
# print("Luas Lingkaran:", daftar_bangun[1].luas())
# print("Keliling Lingkaran:", daftar_bangun[1].keliling())


class BangunDatar:
    def luas(self):
        return 0
    def keliling(self):
        return 0
    
class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi
    def luas(self):
        return self.sisi * self.sisi
    def keliling(self):
        return 4 * self.sisi
    
class Lingkaran(BangunDatar):
    def __init__(self, r):
        self.r = r
    def luas(self):
        return 3.14 * self.r * self.r
    def keliling(self):
        return 2 * 3.14 * self.r
    
daftar_bangunan = [Persegi(5), Lingkaran(7)]
print("Luas Persegi:", daftar_bangunan[0].luas())
print("Keliling Persegi:", daftar_bangunan[0].keliling())
print("Luas Lingkaran:", daftar_bangunan[1].luas())
print("Keliling Lingkaran:", daftar_bangunan[1].keliling())