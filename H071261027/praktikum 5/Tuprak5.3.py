
ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_sandi(ch, k):
    huruf_kecil = ch.lower()

    if huruf_kecil in ALFABET:
        posisi = ALFABET.find(huruf_kecil)
        posisi_baru = (posisi + k) % 26
        hasil = ALFABET[posisi_baru]

        if ch.isupper():
            return hasil.upper()
        else:
            return hasil

    return ch


def mesin_enkripsi(teks, k):
    hasil = ""

    for ch in teks:
        hasil = hasil + cek_sandi(ch, k)

    return hasil


def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)


def retas_sandi(sandi, kata_kunci):
    hasil = []

    for k in range(26):
        pesan = mesin_dekripsi(sandi, k)

        if pesan.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan))

    return hasil


pesan = input("Masukkan pesan: ")
kunci = int(input("Masukkan kunci: "))

sandi = mesin_enkripsi(pesan, kunci)
print("Pesan terenkripsi:", sandi)
print("Pesan terdekripsi:", mesin_dekripsi(sandi, kunci))

cipher = input("Masukkan pesan tersandi: ")
kata_kunci = input("Masukkan kata kunci target: ")

print("Hasil peretasan:", retas_sandi(cipher, kata_kunci))
