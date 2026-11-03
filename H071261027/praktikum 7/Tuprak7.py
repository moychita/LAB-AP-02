
import os
import random
from datetime import datetime


if not os.path.exists("invoices"):
    os.mkdir("invoices")


def buat_invoice():
    nama_kasir = input("Nama kasir: ")
    produk = []
    total = 0

    while True:
        nama_produk = input("Nama produk: ")
        harga = int(input("Harga produk: "))
        jumlah = int(input("Jumlah produk: "))

        subtotal = harga * jumlah
        total += subtotal

        produk.append(
            [nama_produk, harga, jumlah, subtotal]
        )

        tambah = input("Tambah produk lagi? (y/t): ")
        if tambah.lower() != "y":
            break

    # buat id
    waktu = datetime.now()
    inisial = ""

    for kata in nama_kasir.split():
        inisial += kata[0].upper()

    id_transaksi = (
        inisial
        + waktu.strftime("%y%m%d%H%M")
        + str(random.randint(100, 999))
    )

    # 
    isi = "========== INVOICE ==========\n"
    isi += "ID Transaksi: " + id_transaksi + "\n"
    isi += "Nama Kasir: " + nama_kasir + "\n"
    isi += "Waktu: " + waktu.strftime("%Y-%m-%d %H:%M:%S") + "\n"
    isi += "-----------------------------\n"

    for item in produk:
        isi += "Produk: " + item[0] + "\n"
        isi += "Harga: Rp " + str(item[1]) + "\n"
        isi += "Jumlah: " + str(item[2]) + "\n"
        isi += "Subtotal: Rp " + str(item[3]) + "\n"
        isi += "-----------------------------\n"

    isi += "TOTAL: Rp " + str(total) + "\n"
    isi += "=============================\n"

    # 
    nama_file = "invoices/" + id_transaksi + ".txt"

    with open(nama_file, "w") as file:
        file.write(isi)

    print("\nTransaksi berhasil!")
    print(isi)

    # riwyat
    if not os.path.exists("trx_history.txt"):
        with open("trx_history.txt", "w") as file:
            file.write(
                "Waktu | ID Transaksi | Nominal Transaksi\n"
            )

    with open("trx_history.txt", "a") as file:
        file.write(
            waktu.strftime("%Y-%m-%d %H:%M:%S")
            + " | " + id_transaksi
            + " | Rp " + str(total) + "\n"
        )


def cari_invoice():
    id_transaksi = input("Masukkan ID transaksi: ")
    nama_file = "invoices/" + id_transaksi + ".txt"

    if os.path.exists(nama_file):
        with open(nama_file, "r") as file:
            isi = file.read()

        print("\n", isi)
    else:
        print("Invoice tidak ditemukan.")


def lihat_riwayat():
    if os.path.exists("trx_history.txt"):
        with open("trx_history.txt", "r") as file:
            print(file.read())
    else:
        print("Belum ada riwayat transaksi.")


while True:
    print("===== APLIKASI KASIR =====")
    print("1. Buat transaksi")
    print("2. Cari invoice")
    print("3. Lihat riwayat transaksi")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        buat_invoice()
    elif pilihan == "2":
        cari_invoice()
    elif pilihan == "3":
        lihat_riwayat()
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
