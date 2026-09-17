menu = ["kopi_susu", "matcha_latte", "americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

#menentukan sub total 
sub_kopi_susu = harga[0] * jumlah[0]
sub_matcha_latte = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

#memasukkan ketiga subtotal kedalam list
subtotal_pendapatan = [sub_kopi_susu, sub_matcha_latte, sub_americano]

#menghitung total seluruh
total_pendapatan = sum(subtotal_pendapatan)

BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_pendapatan - BIAYA_OPERASIONAL

#menghitung jumlah barang yang terjual
total_barang_terjual = sum(jumlah)

target_tercapai = total_pendapatan > 200000 and total_barang_terjual > 10

print(f"subtotal kopi susu : {sub_kopi_susu}")
print(f"subtotal matcha latte : {sub_matcha_latte}")
print(f"subtotal americano : {sub_americano}") 
print(f"total pendapatan : {sum(subtotal_pendapatan)}")
print(f"pendapatan bersih : {pendapatan_bersih}")
print(f"total barang terjual : {total_barang_terjual}")
print(f"target tercapai : {target_tercapai}")
