teks = input("Masukkan kode prasasti: ").lower()

def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    teks_bersih = ""
    for huruf in teks:
        if huruf in alfabet:
            teks_bersih += huruf

    return teks_bersih


def cek_palinrome(teks):
    teks_balik = "".join(reversed(teks))
    if teks == teks_balik:
           return True
    for i in range(len(teks)):
        if teks[i] != teks_balik[i]:
            return False

def inti_palinrome(teks):
    panjang_maks = 0
    hasil = ""
    indeks_awal = 0

    for i in range(len(teks)):
        for j in range(len(teks), i, -1):
            substring = teks[i:j]

            status = cek_palinrome(substring)

            if status and len(substring) > panjang_maks:
                hasil = substring
                panjang_maks = len(substring)
                indeks_awal = i

    return {
        "teks": hasil,
        "panjang": panjang_maks,
        "indeks_awal": indeks_awal
    }

teks_bersih = bersihkan_teks(teks)
hasil = inti_palinrome(teks_bersih)

print("Teks bersih:", teks_bersih)
print("Hasil:", hasil)