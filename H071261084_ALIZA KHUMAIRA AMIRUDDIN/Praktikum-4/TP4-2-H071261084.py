def hitung_nilai_ujian(*args):
    total = sum(args)
    jumlah_data = len(args)
    rata_rata = total / jumlah_data
    nilai_tertinggi = max(args)
    nilai_terendah = min(args)
    return rata_rata, nilai_tertinggi, nilai_terendah

nilai = []
while True:
    masukkan_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai):  ")
    if masukkan_nilai == "":
        break
    try: 
        nilai_ujian = float(masukkan_nilai)
        if nilai_ujian < 0 or nilai_ujian > 100:
            print("Minimal nilai adalah 0 dan maksimal nilai adalah 100")
            continue
        nilai.append(nilai_ujian)
    except ValueError:
            print("Nilai harus berupa angka")

if len(nilai) == 0:
    print("Data nilai tidak tersedia")
else:
    rata_rata, nilai_tertinggi, nilai_terendah = hitung_nilai_ujian(*nilai)
    print(f"Rata-rata kelas: {rata_rata}")
    print(f"Nilai tertinggi: {nilai_tertinggi}")
    print(f"Nilai terendah: {nilai_terendah}")