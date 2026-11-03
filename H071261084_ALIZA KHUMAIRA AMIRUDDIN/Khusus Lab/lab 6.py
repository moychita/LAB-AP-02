# # buah = ["Apel", "Jeruk", "Mangga"]

# # print(buah[0])

# # buah.append("Pisang")
# # print(buah)

# angka = [30, 10, 20]
# angka.insert(1,15)
# # angka.remove(30)
# # angka.pop(0)]

# angka.sort()
# print(angka)

# angka = [10, 20, 30, 40, 50, 60]

# print(angka[1:4])
# print(angka[::2])
# print(angka[::-1])

# angka = [70, 80, 90, 75, 85]
# angka.append(95)
# angka.insert(2, 88)
# angka.pop(0)

# print(angka)
# print(angka[1:5:2])

# nilai = [[80, 90], [75, 85]]
# print(nilai[0][1])

# angka = [1, 2, 3, 4, 5, 6]
# hasil = [x**2 for x in angka if x % 2 == 0]
# print(hasil)


# nilai = [60, 75, 90, 55, 85]
# jumlah = [x for x in nilai if x >= 75]

# print(jumlah)
# print(len(jumlah))

# bahasa =("Python", "Java", "C++")
# print(bahasa[0])

# data = ("Pyhton", True, 1)
# ubah = list(data)
# ubah[1] = False
# data = tuple(ubah)

# print(data)


# data = ("Lab Dasar", "Lab Jaringan", "Lab Pemrograman")
# ubah = list(data)
# ubah[1] = "Lab Multimedia"
# terbaru = tuple(ubah)

# print(f"dimulai dari: {data[-1]}") 
# print(terbaru)

# angka = {1, 2, 2, 3, 3}
# print(angka)

# angka.add(4)
# angka.add(4)
# print(angka)

# a = {1, 2, 3, 4}
# b = {3, 4, 5}

# print(a | b)
# print(a & b)
# print(a - b)
# print(a ^ b)

# a = {101, 102, 103, 104}
# b = {103, 104, 105, 106}
# print(f"Semua peserta: {a | b}")
# print(f"Peseta kedua kelas: {a & b}")
# print(f"Khusus kelas A: {a - b}")


# mahasiswa = {
#     "nama": "nurul",
#     "nilai": {"mtk":80, "bing": 90}
# }
# mahasiswa["nilai"] ["mtk"] = 90
# mahasiswa["nilai"] ["fisika"] = 75
# mahasiswa.pop("nama")

# print(mahasiswa)


# mahasiswa = {
#     "Nama": "Sari", "Nilai": {
#         "Matematika" : 80, "Bahasa Inggris" : 90,
#     }
# }
# mahasiswa["Nilai"] ["Matematika"] += 10
# mahasiswa["Nilai"] ["Fisika"] = 75
# mahasiswa.pop("Nama")

# print(mahasiswa)


with open("test.txt", "r") as f:
    data = f.read
    print(data)