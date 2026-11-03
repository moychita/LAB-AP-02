import re

def validasi_nim(nim):
    pattern = r'H071[0-9]{6}$'
    if re.match(pattern, nim):
        return "NIM valid"
    else:
        return "Format NIM tidak valid"

def validasi_email(email):
    pattern2 = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    if re.match(pattern2, email):
        return "Email valid"
    else:
        return "Format email tidak valid"

def validasi_nomor(nomor):
    pattern3 = r'^[0-9]{10,13}$'
    if re.match(pattern3, nomor):
        return "Nomor telepon valid"
    else:
        return "Format nomor telepon tidak valid"

print("=====validasi data mhs=====")
nim = input("Masukkan NIM: ")
email = input("Masukkan email: ")
nomor = input("Masukkan nomor telepon: ")

print("-----Hasil Validasi-----")

print(f'NIM: {validasi_nim(nim)}')
print(f'Email: {validasi_email(email)}')
print(f'Nomor Telepon: {validasi_nomor(nomor)}')

if validasi_email(email) and validasi_nomor(nomor) and validasi_nim(nim):
    print("Data mahasiswa berhasil diverifikasi!")
else:
    print("Data mahasiswa tidak valid!")