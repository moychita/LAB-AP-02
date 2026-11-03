
def cek_kata(teks, kata):
    indeks = []
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    awal = 0

    while True:
        posisi = teks_kecil.find(kata_kecil, awal)

        if posisi == -1:
            break

        indeks.append(posisi)
        awal = posisi + 1

    return indeks


def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyz"

    if i > 0:
        sebelum = teks[i - 1].lower()

        if sebelum in alfabet:
            return False

    akhir = i + panjang

    if akhir < len(teks):
        sesudah = teks[akhir].lower()

        if sesudah in alfabet:
            return False

    return True


def sensor_kata(teks, kata, simbol):
    indeks_kata = cek_kata(teks, kata)
    indeks_valid = []

    for i in indeks_kata:
        if cek_batas_kata(teks, i, len(kata)):
            indeks_valid.append(i)

    hasil = ""
    i = 0
    jumlah = 0

    while i < len(teks):
        if i in indeks_valid:
            for j in range(len(kata)):
                hasil = hasil + simbol

            i = i + len(kata)
            jumlah = jumlah + 1
        else:
            hasil = hasil + teks[i]
            i = i + 1

    return hasil, jumlah, indeks_valid


teks = input("Masukkan teks: ")
kata = input("Kata yang disensor: ")
simbol = input("Simbol sensor: ")

hasil = sensor_kata(teks, kata, simbol)

print("Teks tersensor:", hasil[0])
print("Jumlah disensor:", hasil[1])
print("Indeks awal:", hasil[2])
