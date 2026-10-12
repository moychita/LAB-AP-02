print("---Setup Denah Bioskop NontonYuk")

while True: 
    try:
        b= int(input("masukkan jumlah baris:"))
        if b < 0:
            print("Jumlah baris harus lebih dari 0!")
            continue

        break
            
    except ValueError:
        print("Input baris harus berupa angka!")

k = int(input("Masukkan jumlah kursi perbaris:"))

print("---Daftar Kursi Tersedia---")

for b in range(1,b+1):
    for k in range(1,k+1):

        if b == 1 and k%2 == 0:
            continue
        elif k == 13:
            continue

        print(f"Baris {b} - Kursi {k}")