teks = input("Masukkan Teks: ").lower ()
kata_target = input("Masukkan kata target: ").lower ()
simbol = input("Masukkan simbol: ")

ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_kata(teks, kata):
    kemunculan_kata = []
    start = 0
    while True:
        posisi = teks.find(kata, start)
        if posisi == -1:
            break
        kemunculan_kata.append(posisi)
        start = posisi + 1
    return kemunculan_kata

def cek_batas_kata(teks, i, panjang):
    if i > 0:
        kata_sebelum = teks[i - 1]
        if kata_sebelum in ALFABET:
            return False
        if i + panjang < len(teks):
            kata_sesudah = teks[i + panjang]
            if kata_sesudah in ALFABET:
                return False
    return True

def sensor_kata(teks, kata, simbol):
    panjang = len(kata)
    indeks_kemunculan = cek_kata(teks, kata)
    indeks_valid = []
    for i in indeks_kemunculan:
        if cek_batas_kata(teks, i, panjang):
            indeks_valid.append(i)

    teks_sensor = ""
    i = 0
    while i < len(teks):
        if i in indeks_valid:
            teks_sensor += simbol * len(kata)
            i += len(kata)
        else:
            teks_sensor += teks[i]
            i += 1
        
    return teks_sensor, len(indeks_valid), indeks_valid
    
teks_tersensor, jumlah_tersensor, list_indeks_awal = sensor_kata(teks, kata_target, simbol)
    
print(f"Hasil Teks: {teks_tersensor}")
print(f"Jumlah Tersensor: {jumlah_tersensor}")
print(f"Indeks: {list_indeks_awal}")