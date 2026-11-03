def rekap_nilai(*args):
    rata_rata = sum(args) / len(args)
    tertinggi = max(args)
    terendah = min(args)

    return rata_rata, tertinggi, terendah


nilai_siswa = []

while True:
    nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")

    if nilai == "":
        break

    nilai_siswa.append(float(nilai))

if len(nilai_siswa) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata, tinggi, rendah = rekap_nilai(*nilai_siswa)

    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tinggi}")
    print(f"Nilai terendah: {rendah}")