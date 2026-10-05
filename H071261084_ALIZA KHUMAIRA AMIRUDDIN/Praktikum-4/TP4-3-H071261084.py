def hitung_mundur(angka):
    print(angka)
    if angka == 0:
        print("Luncurkan!")
    else:
        hitung_mundur(angka - 1)

while True:
    try:
        angka_awal = int(input("Masukkan angka awal hitung mundur: "))
        if angka_awal < 0:
            print("Input tidak valid, angka tidak boleh negatif")
        else:
            break
    except:
        print("Harus berupa angka tabe'!")
        continue

hitung_mundur(angka_awal)
