
def bersihkan_text(text):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""
    for huruf in text:
        huruf = huruf.lower()

        if huruf in alfabet:
            hasil += huruf
    
    return hasil

def cek_palinrome(text):
    balik = "".join(reversed(text))
    if text == balik:
        return True, -1
    else:
        for i in range(len(text)):
            if text[i] != balik[i]:
                return False, i

def inti_palinrome(text):
    terpanjang = ""
    text = bersihkan_text(text)
    palindrom_terpanjang = ""
    indeks_awal = 0

    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            substring = text[i:j]
            hasil = cek_palinrome(substring)

            if hasil[0] == True:
                if len(substring) > len(palindrom_terpanjang):
                    palindrom_terpanjang = substring
                    indeks_awal = i

    return {
        "teks": palindrom_terpanjang,
        "panjang": len(palindrom_terpanjang),
        "indeks_awal": indeks_awal
    }

print(inti_palinrome("Raja 123 ajar, babad mati!"))