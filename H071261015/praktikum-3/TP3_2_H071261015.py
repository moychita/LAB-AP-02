while True:
    try:
        N = int(input("masukkan jumlah baris: "))
        if N <= 0:
            print("input harus angka!")
            continue
        break
    except ValueError:
        print("input harus berupa angka!")
        
while True:
    try:
        M = int(input("masukkan jumlah kursi per baris: "))
        if M <= 0:
            print("input harus berupa angka!")
            continue
        break
    except ValueError:
        print("input harus berupa angka!")
        

print("--- daftar kursi tersedia ---")        
for baris in range(1, N + 1):
    for kursi in range(1, M + 1):
        
        if kursi == 13:
            continue
        
        elif baris == 1 and kursi %2 == 0:
            continue
        
        print(f"baris {baris} - kursi {kursi} ")
        
        
        
        
    