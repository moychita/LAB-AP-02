class Rekening:
    def __init__(self, nomor, pemilik, saldo):
        self.nomor = nomor
        self.pemilik = pemilik
        self.saldo = saldo

    def setoran(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
        else:
            print("Jumlah setoran harus positif")

    def penarikan(self, jumlah):
        if jumlah <= 0:
            print("Jumlah penarikan harus positif")
        elif jumlah > self.saldo:
            print("Saldo tidak mencukupi")
        else:
            self.saldo -= jumlah

    def transfer(self, tujuan, jumlah):
        if tujuan == self:
            print("Tidak bisa transfer ke rekening sendiri")
        elif jumlah <= 0:
            print("Jumlah transfer harus positif")
        elif jumlah > self.saldo:
            print("Saldo tidak mencukupi")
        else:
            self.saldo -= jumlah
            tujuan.saldo += jumlah
            print("Transfer berhasil")


r1 = Rekening("001", "Ayu", 500000)
r2 = Rekening("002", "Bima", 100000)

r1.transfer(r2, 150000)

print("Saldo Ayu:", r1.saldo)
print("Saldo Bima:", r2.saldo)