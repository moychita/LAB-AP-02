persentase = int(input("Masukkan persentase cabai (1-100): "))
if persentase < 0 or persentase > 100:
    print("Tidak valid.")
elif 11 <= persentase <= 40:
    print("Level Sedang.")
elif 0 <= persentase <=10:
    print("Level Aman.")
elif 41 <= persentase <= 70:
    print("Level Tinggi.")
else:
    print("Level Ekstrem.")