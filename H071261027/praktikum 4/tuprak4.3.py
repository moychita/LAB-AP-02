def hitung_mundur(angka):
    if angka < 0:
        print("Input tidak valid, angka tidak boleh negatif.")
        return

    print(angka)

    if angka == 0:
        print("Luncurkan!")
        return

    hitung_mundur(angka - 1)


while True:
    angka_awal = int(input("Masukkan angka awal hitung mundur: "))

    if angka_awal >= 0:
        break
    else:
        print("Input tidak valid, angka tidak boleh negatif.")

hitung_mundur(angka_awal)