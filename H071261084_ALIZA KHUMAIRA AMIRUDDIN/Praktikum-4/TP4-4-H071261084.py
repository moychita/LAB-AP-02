print("=== Konversi Suhu ===")

def konversi_suhu(suhu, skala_asal, skala_tujuan):
    if skala_asal not in ["C", "F", "K"] and skala_tujuan not in ["C", "F", "K"]:
        raise ValueError ("Skala suhu tidak dikenali")
    if skala_asal == skala_tujuan:
        return suhu
    elif skala_asal == "C" and skala_tujuan == "F":
        return (suhu * 9/5) + 32
    elif skala_asal == "C" and skala_tujuan == "K":
        return suhu + 273.15
    elif skala_asal == "F" and skala_tujuan == "C":
        return (suhu - 32)*5/9
    elif skala_asal == "F" and skala_tujuan == "K":
        return (suhu - 32)*5/9 + 273.15
    elif skala_asal == "K" and skala_tujuan == "C":
        return suhu - 273.15
    elif skala_asal == "K" and skala_tujuan == "F":
        return (suhu - 273.15)*9/15 + 32

while True:
    masukan_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar: ")
    if masukan_suhu == "selesai":
        break
    try:
        suhu = float(masukan_suhu)
    except ValueError:
        print("Error: Suhu harus berupa angka")
        continue
    try:
        skala_asal = input("Skala asal (C/F/K): ").upper()
        skala_tujuan = input("Skala tujuan (C/F/K): ").upper()
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {suhu} {skala_asal} = {hasil} {skala_tujuan}")
    except ValueError:
        print("Error: Skala suhu tidak dikenali")