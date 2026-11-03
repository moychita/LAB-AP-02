class Mahasiswa:
    def __init__(self, nim, nama, daftar_tugas, UTS, UAS):
        self.nim = nim
        self.nama = nama
        self.daftar_tugas = daftar_tugas
        self.UTS = UTS
        self.UAS = UAS

    def status(self):
        for i in self.daftar_tugas:
            if i > 100:
                return "Nilai tidak boleh lebih dari 100"
                
        if self.UTS > 100 or self.UAS > 100:
            return "Nilai tidak boleh lebih dari 100"
            
        if self.daftar_tugas:
            nilai_uas = self.UAS * 40 // 100
            nilai_uts = self.UTS * 30 // 100
            rata_rata_tugas = sum(self.daftar_tugas) / len(self.daftar_tugas)
            nilai = nilai_uas + nilai_uts + rata_rata_tugas
        else:
            nilai = 0
            
        if nilai >= 60:
            return "Lulus brok"
        else:
            return "Tidak lulus bro"

m = Mahasiswa("H07161084", "Aliza", )