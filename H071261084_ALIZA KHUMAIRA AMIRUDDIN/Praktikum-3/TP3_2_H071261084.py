print("---Setup Denah Bioskop NontonYuk---")

while True:
    try:
      baris = int(input("Masukkan jumlah baris: "))
      if baris <= 0:
         print("Jumlah baris harus lebih dari 0!")
      else:
         break
    except:
       print("Input baris harus berupa angka")

while True:
    try:
      kursi = int(input("Masukkan jumlah kursi per baris: "))
      if kursi <= 0:
         print("Jumlah baris harus lebih dari 0!")
      else:
         break
    except:
       print("Input baris harus berupa angka")

for baris in range(1, baris + 1):
   for kursi in range (1, kursi + 1):
      if kursi == 13:
         continue
      if baris == 1 and kursi % 2 == 0:
         continue
      print(f"Baris {baris} - Kursi {kursi}")
   print()

    
      
   
    