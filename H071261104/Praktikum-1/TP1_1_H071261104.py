menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

subtotal_kopi = harga[0] * jumlah[0]
subtotal_matcha = harga[1] * jumlah[1]
subtotal_americano = harga [2] * jumlah[2]

subtotal_pendapatan = [subtotal_matcha, subtotal_kopi, subtotal_americano]
total_pendapatan = sum(subtotal_pendapatan)
biaya_operasional = 15000

pendapatan_bersih = total_pendapatan - biaya_operasional

terjual = sum(jumlah)

if total_pendapatan >= 200000 and terjual >= 10:
    target = "Tercapai"

print("Subtotal:", total_pendapatan)
print("Pendapatan Bersih:", pendapatan_bersih)
print("Hasil Target:", target)