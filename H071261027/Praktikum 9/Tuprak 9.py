class Pemain:
    def __init__(self, nama, id, role, kill, assist, objective):
        self.nama = nama
        self.id = id
        self.role = role
        self.kill = kill
        self.assist = assist
        self.objective = objective

    def hitung_skor_akhir(self):
        skor = (0.3*self.kill)+(0.3*self.assist)+(0.4*self.objective)
        return skor

    def status_performa(self):
        if self.hitung_skor_akhir >= 60:
            return "unggul"
        else:
            return "perlu evaluasi"

    def tampilkan_data(self):
        return f"{nama:<15}{id:<12}{role:<12}{kill:<12}{assist:<12}{objective}"

print("===SISTEM PENILAIAN PERFORMA PEMAIN===")
jumlah_pemain = []
jumlah = int(input("Maukkan jumlah pemain: "))

for i in range(jumlah):
    print(f"---Data pemain ke-{i+1}")
    nama = input("Nama: ")
    id = input("ID: ")
    role = input("Role: ")
    kill = int(input("Nilai Kill: "))
    assist = int(input("Nilai Assist: "))
    objective = int(input("Nilai Objective:"))
    pemain = Pemain(nama, id, role, kill, assist, objective)
    jumlah_pemain.append(pemain)    

print("===REKAPITULASI PERFORMA PEMAIN===")
print("="*50)
print(f"{'Nama':<15}{'ID':<12}{'Role':<12}{'Skor':<12}{'Status'}")
print("="*50)
for i in jumlah_pemain:
    print(i.tampilkan_data())