# # # # # nim = input("Masukkan nim: ")
# # # # # panjang = len(nim)

# # # # # kode_fakultas = nim[0]
# # # # # if len(nim) != 10:
# # # # #     raise ValueError("Nim tidak valid")
# # # # #     print("Masukkan nim yang benar")

# # # # #     if kode_fakultas == "H":
# # # # #         fakultas = "FMIPA"
# # # # #     if  kode_fakultas == "E":
# # # # #         fakultas == "FISIP"
# # # # #     if kode_fakultas == "B":
# # # # #         fakultas == "Hukum"


# # # # # print("Panjang hurufnya adalah", (panjang))
# # # # # print("Panjang hurufnya adalah", (kode_fakultas))
# # # # # print("Panjang hurufnya adalah", (fakultas))


# # # # nim = input("Masukkan nim: ")
# # # # tahun_angkatan = nim[4:6]

# # # # print(f"Tahun angkatan {tahun_angkatan}")


      
# # # # # nim = input("Masukkan nim: ")
# # # # # tahun_angkatan = nim[4:6]

# # # # # print(f"Tahun angkatan {tahun_angkatan}")







# # # # # matkul = "database"
# # # # # jumlah = matkul.count("a")
# # # # # print(f"Karakter a pada 'database' muncul sebanyak {jumlah} kali")


# # # # while True:
# # # #     password = input("Masukkan password: ")
# # # #     if password.count(" ") > 0:
# # # #         print("Error Password tidak boleh mengandung spasi")
# # # #     elif len(password) < 8:
# # # #         print("Password minimal 8 karakter")
# # # #     else: 
# # # #         print("Password valid dan berhasil disimpan")
# # # #         break

# # # # # karakter = "Rp"
# # # # # cari = nama.find(karakter)

# # # # # print(f"Harga (Rp) mulai terdeteksi di indeks ke: {cari}")

# # # word = "hello world"
# # # baru = word.replace("world", "halo")
# # # print(baru)

# # while True:
# #     email = input("Masukkan email: ")
# #     if email.endswith(".unhas.ac.id"):
# #         print("Akses diterima")
# #         break
# #     else:
# #         print("Akses ditolak! Gunakan email resmi.")

# kata = input("Masukkan kata: ")
# balik = "". join(reversed(kata))
# print(f"balik: {balik}")

# def cek_palindrom(kata):
#     if kata == balik:
#         return kata
#     if kata != balik:
#         return kata

# cek_palindrom(kata)

toko = "Toko "
nama = input("Masukkan nama cabang:  ")
semuanya = toko + nama
jumlah = "-" *len(semuanya)

print(jumlah)
print(semuanya)
print(jumlah)
