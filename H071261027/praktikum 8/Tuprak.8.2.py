import re

username_valid = []

def validasi_username(nama):
    pattern = r"^[a-zA-Z][A-Za-z0-9_]{4,11}$"
    return re.match(pattern, nama)

while True:
    nama = input("Masukkan username: ")
    if nama.upper() == "SELESAI":
        break

    if validasi_username(nama):
        username_valid.append(nama)
        print("Username tersedia")

    else:
        print("username tidak tersedia")

for i in username_valid:
    i =+ 1
print ("=== Rekapitulasi===")
print ("Username valid:")
print (f"{i}. {username_valid[i-1]} ")
print (f"Jumlah Username valid: {len(username_valid)}")

# {enumerate.username_valid}{start=}"