# class Mahasiswa:
#     def __init__(self, nama, nim, program_studi):
#         self.nama = nama
#         self.nim = nim
#         self.program_studi = program_studi

# mahasiswa1 = Mahasiswa("Andi", "H071261084", "Sistem Informasi")
# print(mahasiswa1.nama)
# print(mahasiswa1.nim)
# print(mahasiswa1.program_studi)

# class Mahasiswa:
#     def __init__(self, nama):
#         self.nama = nama
#     def sapa(self):
#         return f"Halo, nama saya {self.nama}"

# mahasiswa1 = Mahasiswa("Andi")
# mahasiswa2 = Mahasiswa("Siti")
# print(mahasiswa1.sapa())
# print(mahasiswa2.sapa())

# class Mahasiswa:
#     def __init__(self, nama, sks_lulus=0):
#         self.nama = nama
#         self.sks_lulus = sks_lulus

#     def tambah_sks(self, jumlah_sks):
#         self.sks_lulus += jumlah_sks
#         print(f"{jumlah_sks} sks berhasil ditambahkan.")

#     def cek_sks(self):
#         return self.sks_lulus

# mahasiswa1 = Mahasiswa("Andi")
# mahasiswa1.tambah_sks(20)
# print("total sks lulus:", mahasiswa1.cek_sks())

# class Dompet:
#     def __init__(self, pemilik, saldo=0):
#         self.pemilik = pemilik
#         self.saldo = saldo

#     def isi_saldo(self, jumlah):
#         self.saldo += jumlah
#         print(f"Saldo {self.pemilik} bertambah Rp{jumlah}.")

#     def cek_saldo(self):
#         return self.saldo
    
# print("=== UJI COBA DOMPET===")
# m1 = Dompet("Andi")
# m1.isi_saldo(25000)
# print("Saldo saat ini: Rp", m1.cek_saldo())

# class Mahasiswa:
#     def __init__(self, nama, nim):
#         self.nama = nama
#         self.nim = nim
#         self.ipk = 0.0
        
#     def perbarui_ipk(self, ipk_baru):
#         if 0 <= ipk_baru <= 4:
#             self.ipk = ipk_baru
#             print(f"IPK {self.nama} diperbarui menjadi {self.ipk}.")
#         else:
#             print("IPK tidak valid. Harus berada dalam rentang 0-4.")
            
# class MahasiswaBerprestasi(Mahasiswa):
#     def __init__(self, nama, nim, prestasi):
#         super().__init__(nama, nim)
#         self.prestasi = prestasi
#     def tampilkan_prestasi(self):
#         print(f"Mahasiswa : {self.nama}")
#         print(f"NIM : {self.nim}")
#         print(f"IPK : {self.ipk}")
#         print(f"Prestasi : {self.prestasi}")
        
# mahasiswa = MahasiswaBerprestasi("Budi", "123456", "Juara 1 Lomba Matematika")
# mahasiswa.perbarui_ipk(3.8)
# mahasiswa.tampilkan_prestasi()


# class Hewan:
#     def suara(self):
#         return "Hewan mengeluarkan suara"

# class Anjing(Hewan):
#     def suara(self):
#         return "Anjing menggongong"

# hewan1 = Hewan()
# anjing1 = Anjing

# class Produk:
#     def __init__(self, nama, harga):
#         self.nama = nama
#         self.harga = harga
        
#     def info(self):
#         return f"{self.nama}: {self.harga}"
      
# class ProdukDiskon(Produk):
#     def __init__(self, nama, harga, diskon):
#         super().__init__(nama, harga)
#         self.diskon = diskon

#     def info(self):
#         harga = self.harga - (self.harga * self.diskon / 100)
#         return f"{self.nama} (diskon): {harga}"

# print(Produk("Mouse", 100000).info())
# print(ProdukDiskon("Keyboard", 285000, 10).info())


class Rekening:
    def __init__(self, saldo):
        self.__saldo = saldo
        
    def tarik(self, jumlah):
        if 0 <= jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Penarikan Rp{jumlah} berhasil.")
        else:
            print("Penarikan ditolak.")

    def cek_saldo(self):
        return f"saldo akhir: Rp{self.__saldo}"
     
apa = Rekening(500000)
apa.tarik(200000)
apa.tarik(900000)
print(apa.cek_saldo())