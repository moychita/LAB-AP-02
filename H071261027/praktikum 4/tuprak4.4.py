
def konversi_suhu(suhu, asal, tujuan):

    if asal == "C":
        celsius = suhu
    elif asal == "F":
        celsius = (suhu - 32) * 5 / 9
    elif asal == "K":
        celsius = suhu - 273.15

    if tujuan == "C":
        return celsius
    elif tujuan == "F":
        return celsius * 9 / 5 + 32
    elif tujuan == "K":
        return celsius + 273.15


print("=== Konversi Suhu ===")

while True:
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")

    if input_suhu.lower() == "selesai":
        break

    try:
        suhu = float(input_suhu)
        asal = input("Skala asal (C/F/K): ").upper()
        tujuan = input("Skala tujuan (C/F/K): ").upper()

        if asal not in ["C", "F", "K"] or tujuan not in ["C", "F", "K"]:
            print("Error: Skala suhu tidak dikenali.")
            continue
        
        hasil = konversi_suhu(suhu, asal, tujuan)

        print(f"Hasil: {suhu} {asal} = {hasil:.1f} {tujuan}")

    except ValueError:
        print("Error: Masukkan suhu berupa angka yang valid.")
