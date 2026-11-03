# import re
# pattern = '^s...a$'
# test_string = 'sama'
# result = re.match(pattern, test_string)

# if result:
#     print("Cocok.")
# else:
#     print("Tidak cocok.")



# import re
# teks = "A, B, D, C, E"
# result = re.findall(r'[ABC]', teks)
# print(result)

# import re
# teks = "kotak, katak, kitak, ktak"
# result = re.findall(r'k.tak', teks)
# print(result)

# import re
# teks = "kapal, kopal, kapur, kopar, kal"
# result = re.findall(r'k...l', teks)
# print(result)

# import re
# teks = "DD 1234 XY adalah mobil saya"
# if re.search(r'^DD', teks):
#     print("Ini plat Makassar")
# else:
#     print("Bukan plat Makassar!")


# import re
# teks = "6281234567890"
# if re.search(f'^08', teks):
#     print("Valid")
# else:
#     print("Tidak Valid")

# import re
# teks = "Gl, Gol, Goool, Goooooool"
# hasil = re.findall (r'Go*l', teks)
# print(hasil)

# import re
# teks = "1,10, 100, 1000"
# hasil = re.findall (r'10*', teks)
# print(hasil)

# import re
# teks = "Gl, Gol, Goool"
# hasil = re.findall (r'Go+l', teks)
# print(hasil)

# import re
# teks = "7, 42, 2024"
# hasil = re.findall (r'[0-9]+', teks)
# print(hasil)

# import re
# teks = "http://google.com, https://yahoo.com"
# hasil = re.findall (r'https?', teks)
# print(hasil)

# import re
# teks = "color, colour, colouur"
# hasil = re.findall (r'colou?r', teks)
# print(hasil)

# import re
# teks = "PTN saya 1234 dan PTN dia 1234567"
# hasil = re.findall (r'\d{4,6}', teks)
# print(hasil)

# import re
# teks = "7, 42, 365"
# hasil = re.findall (r'\d{2,3}', teks)
# print(hasil)

# import re
# teks = "Meja 1 kopi, meja 2 susu, meja 3 teh."
# hasil = re.findall (r'kopi|teh', teks)
# print(hasil)

# import re
# teks = "Senin, Sabtu, Minggu, Rabu"
# hasil = re.findall (r'Sabtu|Minggu', teks)
# print(hasil)

# import re
# teks = "file_saya.pdf, tugas.doc, tugas.docx"
# hasil = re.findall (r'tugas\.(docx?)', teks)
# print(hasil)

# import re
# teks = "ayam goreng, ayam bakar, bebek goreng"
# hasil = re.findall (r'ayam.(goreng|bakar)', teks)
# print(hasil)

# import re
# teks = "Harganya adalah $100 dollar."
# hasil = re.findall (r'\$\d+', teks)
# print(hasil)

# import re
# teks = "3.14 dan 3x14"
# hasil = re.findall (r'\d\d+', teks)
# print(hasil)

# import re
# print(re.findall(r'Athe', "the sun"))
# print(re.findall(r'Athe', "seen the sun"))

# import re
# print(re.findall(r'\AHalo', "Halo Dunia"))
# print(re.findall(r'\AHalo', "Selamat, Halo"))

# import re
# teks = "cat in the category"
# print(re.findall(r'\bcat\b', teks))
# print(re.findall(r'\Bcat', "education"))

# import re
# teks = "Call 0812345 now"
# print(re.findall(r'\d', teks))
# print(re.findall(r'\D', teks))

# import re
# teks = "Order A17 dan B205"
# print(re.findall(r'\d+', teks))

# import re
# teks = "Python RegEx"
# print(re.findall(r'\s', teks))
# print(re.findall(r'\S+', teks))

# import re
# teks = "Belajar regex itu seru"
# x = re.findall(r'\s', teks)
# print(len(x))

# import re
# teks = "user_01 !!!"
# print(re.findall(r'\w+', teks))

# import re
# teks = "Kopi Rp15000, Teh Rp8000, Roti Rp12000"
# print(re.findall(r'^Rp', teks))

# import re
# teks = "apel, jeruk; mangga. pisang"
# hasil = re.split(r'[,:.]+', teks)
# print(hasil)

# import re
# teks = "Dasar kamu gila dan gila!"
# hasil = re.sub(r'gila', 'baik', teks)
# print(hasil)

# import re
# teks = "Dasar kamu gila dan gila!"
# hasil = re.subn(r'gila', '***', teks)
# print(hasil(0))