
def deteksi_anomali_email(email):
    error = []

    if email.count("@") != 1:
        error.append("Email harus memiliki tepat satu @")

    if " " in email:
        error.append("Email tidak boleh mengandung spasi")

    if email.count("@") == 1:
        bagian = email.split("@")
        local = bagian[0]
        domain = bagian[1]

        if local == "" or domain == "":
            error.append("Bagian local dan domain tidak boleh kosong")

        if local != "":
            if local[0] == "." or local[-1] == ".":
                error.append("Bagian local tidak boleh diawali atau diakhiri titik")

            if ".." in local:
                error.append("Bagian local tidak boleh memiliki titik berurutan")

        if domain != "":
            if "." not in domain:
                error.append("Domain harus memiliki minimal satu titik")

            if ".." in domain:
                error.append("Domain tidak boleh memiliki titik berurutan")

            if domain[-1] == ".":
                error.append("Domain tidak boleh diakhiri titik")

        email_kecil = email.lower()

        if not (email_kecil.endswith(".com") or email_kecil.endswith(".id") or email_kecil.endswith(".ac.id")):
            error.append("Email harus berakhiran .com, .id, atau .ac.id")

    return error

# #############################3
def cetak_daftar(daftar_email_valid, karakter_border):
    panjang = 0

    for email in daftar_email_valid:
        if len(email) > panjang:
            panjang = len(email)

    lebar = panjang + 4
    border = karakter_border * lebar

    hasil = border + "\n"

    for email in daftar_email_valid:
        hasil = hasil + "| " + email

        for i in range(panjang - len(email)):
            hasil = hasil + " "

        hasil = hasil + " |\n"

    hasil = hasil + border

    return hasil


daftar_email_valid = []

while True:
    email = input("Masukkan email (ketik tutup untuk selesai): ")

    if email.lower() == "tutup":
        break

    error = deteksi_anomali_email(email)
##########################3####
    if email.lower() in [e.lower() for e in daftar_email_valid]:
        error.append("Email tidak boleh duplikat")

    if len(error) == 0:
        daftar_email_valid.append(email)
        print("Email valid!")
    else:
        print("Email tidak valid:")

        for masalah in error:
            print("-", masalah)

print("Daftar email valid:")
print(cetak_daftar(daftar_email_valid, "*"))
