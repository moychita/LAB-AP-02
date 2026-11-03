# f = open("file.txt", "r")
# print(f.closed)

# try:
#     with open("file_rahasia.txt", 'r') as f:
#         data = f.read()
#         print(data)
# except:
#     print("Error: Bekas file_rahasia_text tidak ada! Program selesai")

# with open("test.txt", "w") as f:
#     for baris in f:
#         print(baris, end=)

# with open("file.txt", "r") as f:
#     list_kalimat = f.readlines()
#     print(list_kalimat)

# with open("file.txt", "r") as f:
#     baris = f.readlines()
#     print("Awal: " (baris[0].strip().upper()) )
#     print("Akhir: ", )

# with open("file.txt", "w") as f:
#     f.write("Hello World!!!")

# with open("file.txt", "a") as f:
#     f.write("Hello World!!!\n")

# with open("teman.txt", "w") as f:
#     f.write("Andi\n")
#     f.write("Budi\n")
#     print("File teman.txt berhasil dibuat")

# with open("teman.txt", "a") as f:
#     f.write("Citra\n")
#     print("File teman.txt berhasil dibuat")

# with open("teman.txt", "r") as file:
#     data = file.read()
#     print(data)

# import os 
# if os.path.exists("kontak.txt"):
#     os.remove("kontak.txt")
#     print("File kontak.txt berhasil dihapus!")
# else:
#     print("File tidak ditemukan")

# with open("file.txt", "a+") as f:
#     f.write("Fera\n")
#     f.seek(0)
#     konten = f.read()
#     print(konten)

# try:
#     with open("file.text", "x") as file:
#         f.write("Saya Keren")
#         f.seek(0)
#         f.read
# except FileNotFoundError as e:
#     print("File txt sudah ada!")

# try:
#     with open("file.text", "x") as file:
#         f.write("Saya Keren")
#         f.seek(0)
#         f.read
# except FileNotFoundError as e:
#     print("File txt sudah ada!")


# with open("test.txt", "r") as file:
#     data = file.read().lower()
#     total = teks.split().count("python")
#     if nilai >
#     for line in data:
#         word = line.split()
#         print("Kata 'pyhton' muncul sebanyak: " )

with open("test.txt", "r") as file_baca, open("lulus.txt", "w") as file_tulis:
    for baris in file_baca:
        data = baris.split()
        if data:
            nama = data[0]
            nilai = int(baris.strip())
            if nilai >= 75:
                file_tulis.write(str(nilai + "\n"))

print("Daftar Mahasiswa lulus berhasil disimpan ke lulus.txt" )
