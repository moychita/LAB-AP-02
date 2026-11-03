username = input("Masukkan username: ")
password = input("Masukkan password: ")

try:
    if password != "rahasia woi":
        raise ValueError("Password salah!")
except ValueError:
    print("Login gagal")
else:
    print("Login berhasil Selamat datang, Aliza npd")
finally:
    print("Sesi login selesai.")
