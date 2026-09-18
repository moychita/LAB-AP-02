persentase_cabai = int(input("Masukkan persentase cabai: "))
if 0 <= persentase_cabai <= 10:
    print("level aman")
elif persentase_cabai <= 40:
    print("level sedang")
elif persentase_cabai <= 70:
    print("level pedas")
elif persentase_cabai <= 100:
    print("level sangat pedas")
else:
    print("level tidak valid")