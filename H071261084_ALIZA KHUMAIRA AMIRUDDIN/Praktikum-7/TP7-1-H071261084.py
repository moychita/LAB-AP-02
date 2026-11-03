import os
import random
from datetime import datetime

if not os.path.exists("invoices"):
    os.mkdir("invoices")

def buat_invoice():
    print("\n===== TRANSAKSI BARU =====")
    nama_kasir = input("Nama kasir: ")
    inisial = "".join(
        nama[0] for nama in nama_kasir.split()
    ).upper()
    daftar_produk = []
    total_transaksi = 0

    while True:
        nama_produk = input("Nama produk: ")
        harga_produk = int(input("Harga produk: Rp "))
        jumlah_produk = int(input("Jumlah produk: "))
        subtotal = harga_produk * jumlah_produk
        produk = (
            nama_produk,
            harga_produk,
            jumlah_produk,
            subtotal
        )
        daftar_produk.append(produk)
        total_transaksi += subtotal
        print("Subtotal: Rp", subtotal)
        tambah = input("Tambah produk lagi? (y/n): ")
        if tambah.lower() != "y":
            break

    waktu_transaksi = datetime.now()

    id_transaksi = (
        inisial
        + waktu_transaksi.strftime("%y%m%d%H%M")
        + str(random.randint(100, 999))
    )

    nama_file = id_transaksi + ".txt"
    lokasi_file = os.path.join("invoices", nama_file)

    with open(lokasi_file, "w", encoding="utf-8") as file:
        file.write("========== INVOICE ==========\n")
        file.write(f"Nama Kasir: {nama_kasir}\n")
        file.write(f"ID Transaksi: {id_transaksi}\n")
        file.write(
            f"Waktu: {waktu_transaksi.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        file.write("=============================\n")

        file.write("Daftar Produk:\n")

        for produk in daftar_produk:
            nama, harga, jumlah, subtotal = produk

            file.write(f"Produk: {nama}\n")
            file.write(f"Harga: Rp {harga}\n")
            file.write(f"Jumlah: {jumlah}\n")
            file.write(f"Subtotal: Rp {subtotal}\n")
            file.write("-----------------------------\n")

        file.write(f"Total Transaksi: Rp {total_transaksi}\n")
        file.write("=============================\n")
        file.write("Terima kasih telah berbelanja!\n")

    with open(lokasi_file, "r", encoding="utf-8") as file:
        print("\n" + file.read())

    catat_riwayat(
        waktu_transaksi,
        id_transaksi,
        total_transaksi
    )

def catat_riwayat(waktu, id_transaksi, nominal):
    nama_file = "trx_history.txt"
    if not os.path.exists(nama_file):
        with open(nama_file, "w", encoding="utf-8") as file:
            file.write(
                f"{'Waktu':<20} | "
                f"{'ID Transaksi':<20} | "
                f"{'Nominal Transaksi':<20}\n"
            )
            file.write("-" * 67 + "\n")

    with open(nama_file, "a", encoding="utf-8") as file:
        file.write(
            f"{waktu.strftime('%Y-%m-%d %H:%M:%S'):<20} | "
            f"{id_transaksi:<20} | "
            f"Rp {nominal:<17}\n"
        )

def cari_invoice():
    print("\n===== CARI INVOICE =====")

    id_transaksi = input("Masukkan ID transaksi: ")

    nama_file = id_transaksi + ".txt"
    lokasi_file = os.path.join("invoices", nama_file)

    if os.path.exists(lokasi_file):
        with open(lokasi_file, "r", encoding="utf-8") as file:
            print("\n" + file.read())
    else:
        print("Invoice tidak ditemukan.")


def tampilkan_riwayat():
    print("\n===== RIWAYAT TRANSAKSI =====")

    nama_file = "trx_history.txt"

    if os.path.exists(nama_file):
        with open(nama_file, "r", encoding="utf-8") as file:
            print(file.read())
    else:
        print("Belum ada riwayat transaksi.")

while True:
    print("\n===== APLIKASI KASIR =====")
    print("1. Membuat transaksi baru")
    print("2. Mencari invoice")
    print("3. Melihat riwayat transaksi")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        buat_invoice()
    elif pilihan == "2":
        cari_invoice()
    elif pilihan == "3":
        tampilkan_riwayat()
    elif pilihan == "4":
        print("Terima kasih. Program kasir selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1-4.")