import re

def validasi_nim(nim):
    return re.fullmatch(r'H071\d{6}', nim) is not None

def validasi_email(email):
    return re.fullmatch(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', email) is not None

def validasi_telepon(telepon):
    return re.fullmatch(r'\d{10,13}', telepon) is not None

print("=== Validasi Data Mahasiswa ===")
print()

nim = input("Masukkan NIM       : ")
email = input("Masukkan Email     : ")
telepon = input("Masukkan No. Telp  : ")

print()
print("--- Hasil Validasi ---")

if validasi_nim(nim):
    print("NIM         : Valid")
else:
    print("NIM         : Tidak valid")

if validasi_email(email):
    print("Email       : Valid")
else:
    print("Email       : Tidak valid")

if validasi_telepon(telepon):
    print("No. Telepon : Valid")
else:
    print("No. Telepon : Tidak valid")

print()

if validasi_nim(nim) and validasi_email(email) and validasi_telepon(telepon):
    print("Data mahasiswa berhasil diverifikasi!")