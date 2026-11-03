
def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre.capitalize())

    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return

    print("=========================================")
    print(f"{'No':<5}{'Judul':<25}{'Artis':<20}{'Genre':<12}{'Durasi'}")
    print("=========================================")

    total_durasi = 0

    for i, lagu in enumerate(playlist, start=1):
        judul, artis, genre, durasi = lagu
        menit = durasi // 60
        detik = durasi % 60
        format_durasi = f"{menit}:{detik:02d}"

        print(
            f"{i:<5}{judul:<25}{artis:<20}"
            f"{genre:<12}{format_durasi}"
        )

        total_durasi += durasi

    print("=========================================")
    jam = total_durasi // 3600
    menit = (total_durasi % 3600) // 60
    detik = total_durasi % 60

    if jam > 0:
        print(
            f"Total durasi playlist: {jam} jam "
            f"{menit} menit {detik} detik"
        )
    else:
        print(
            f"Total durasi playlist: "
            f"{menit} menit {detik} detik"
        )


def filter_genre(playlist, genre_target):
    hasil = [
        lagu for lagu in playlist
        if lagu[2].lower() == genre_target.lower()
    ]

    return hasil


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak valid!")
    else:
        lagu = playlist.pop(nomor - 1)
        print(f"Lagu '{lagu[0]}' berhasil dihapus!")


def statistik_playlist(playlist, genre_set):
    print("=========================================")
    print("   STATISTIK PLAYLIST PLAYTUNE")
    print("=========================================")

    print(f"Total lagu   : {len(playlist)}")
    print(f"Jumlah genre : {len(genre_set)}")
    print(f"Daftar genre : {genre_set}")

    if len(playlist) == 0:
        print("Playlist masih kosong.")
        print("=" * 40)
        return

    distribusi = {}

    for lagu in playlist:
        genre = lagu[2]
        if genre in distribusi:
            distribusi[genre] += 1
        else:
            distribusi[genre] = 1

    print("\nDistribusi genre:")

    for genre, jumlah in distribusi.items():
        print(f"  {genre:<12}: {'#' * jumlah} ({jumlah})")

    lagu_terpanjang = playlist[0]
    lagu_terpendek = playlist[0]

    for lagu in playlist:
        if lagu[3] > lagu_terpanjang[3]:
            lagu_terpanjang = lagu

        if lagu[3] < lagu_terpendek[3]:
            lagu_terpendek = lagu

    durasi_panjang = (
        f"{lagu_terpanjang[3] // 60}:"
        f"{lagu_terpanjang[3] % 60:02d}"
    )

    durasi_pendek = (
        f"{lagu_terpendek[3] // 60}:"
        f"{lagu_terpendek[3] % 60:02d}"
    )

    print(
        f"\nLagu terpanjang: {lagu_terpanjang[0]} "
        f"({durasi_panjang})"
    )
    print(
        f"Lagu terpendek : {lagu_terpendek[0]} "
        f"({durasi_pendek})"
    )
    print("=" * 40)



playlist = []
genre_set = set()

while True:
    print("\n========================================")
    print("       PLAYLIST MUSIK - PLAYTUNE")
    print("========================================")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        judul = input("Judul lagu: ")
        artis = input("Artis: ")
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip().capitalize()

        try:
            durasi = int(input("Durasi (dalam detik): "))

            if durasi <= 0:
                print("Durasi harus berupa angka positif!")
            else:
                tambah_lagu(
                    playlist, genre_set, judul,
                    artis, genre, durasi
                )

        except ValueError:
            print("Error! Durasi harus berupa bilangan bulat.")

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        if len(genre_set) == 0:
            print("Belum ada genre dalam playlist.")
        else:
            print("Genre tersedia:", genre_set)
            genre_target = input(
                "Masukkan genre yang ingin difilter: "
            ).strip()

            hasil = filter_genre(playlist, genre_target)

            if len(hasil) > 0:
                print(f"\nLagu bergenre '{genre_target}':")

                for i, lagu in enumerate(hasil, start=1):
                    judul, artis, genre, durasi = lagu
                    menit = durasi // 60
                    detik = durasi % 60

                    print(
                        f"  {i}. {judul} - {artis} "
                        f"({menit}:{detik:02d})"
                    )
            else:
                print("Tidak ada lagu dengan genre tersebut.")

    elif pilihan == "4":
        tampilkan_playlist(playlist)

        if len(playlist) > 0:
            try:
                nomor = int(
                    input("Nomor lagu yang ingin dihapus: ")
                )
                hapus_lagu(playlist, nomor)

               
                genre_set = set()

                for lagu in playlist:
                    genre_set.add(lagu[2])

            except ValueError:
                print("Error! Nomor harus berupa bilangan bulat.")

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid! Silakan pilih menu 1-6.")
