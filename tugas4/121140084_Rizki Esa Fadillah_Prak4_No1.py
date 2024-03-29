"""
Nama : Rizki Esa Fadillah
NIM    : 121140084
Kelas  : Praktikum PBO - RB

Tugas 4 => Nomor 1

=== ~ Single Inheritence ~ ==
"""
# Class induk
class Komputer:
    Total_Harga = 0
    def __init__(self, nama, jenis, harga, merk):
        self. nama = nama
        self. jenis = jenis
        self. harga = harga
        self.merk = merk

    def info(self):
        Komputer.Total_Harga += self.harga
        return (f"{self.nama} = {self.jenis} produksi {self.merk}")
    
    def Biaya_Rakit(self):
        return (f"Biaya Rakit Komputer = Rp. {Komputer.Total_Harga}")

# Class turunan dari induk(Komputer)
class Processor (Komputer):
    def __init__(self, nama, jenis, harga, merk, jumlah_core, kecepatan_processor):
        Komputer.__init__(self, nama, jenis, harga, merk)
        self. jumlah_core = jumlah_core
        self. kecepatan_processor = kecepatan_processor

# Class turunan dari induk(Komputer)
class RAM(Komputer):
    def __init__(self, nama, jenis, harga, merk, capacity_RAM):
        Komputer.__init__(self, nama, jenis, harga, merk)
        self. capacity_RAM = capacity_RAM

# Class turunan dari induk(Komputer)
class HDD(Komputer):
    def __init__(self, nama, jenis, harga, merk, capacity_HDD, rpm):
        Komputer.__init__(self, nama, jenis, harga, merk)
        self. capacity_HDD = capacity_HDD
        self. rpm = rpm

# Class turunan dari induk(Komputer)
class VGA(Komputer):
    def __init__(self, nama, jenis, harga, merk, capacity_VGA):
        Komputer.__init__(self, nama, jenis, harga, merk)
        self. capacity_VGA = capacity_VGA

# Class turunan dari induk(Komputer)
class PSU(Komputer):
    def __init__(self, nama, jenis, harga, merk, daya):
        Komputer.__init__(self, nama, jenis, harga, merk)
        self. daya = daya

# Kumpulan objek komponen komputer om Bambang (instance variable)
p1 = Processor("Processor", "Core i7 7740x", 4350000, "Intel", 4 ,"4.3GHz")
p2 = Processor("Processor", "Ryzen 5 3600", 250000, "AMD", 4, "4.3GHz")
ram1 = RAM("RAM", "DDR4 SODimm PC19200/2400MHz", 328000, "V-Gen", "4GB")
ram2 = RAM("RAM", "DDR4 2400MHz", 328000, "G.SKILL", "4GB")
hdd1 = HDD("HDD", "HDD 2.5 inch", 295000, "Seagate", "500GB", 7200)
hdd2 = HDD("HDD", "HDD 2.5 inch", 295000, "Seagate",  "1000GB", 7200)
vga1 = VGA("VGA", "VGA GTX 1050", 250000, "Asus", "2GB")
vga2 = VGA("VGA", "1060Ti", 250000, "Asus",  "8GB")
psu1 = PSU("PSU", "Corsair V550", 250000, "Corsair", "500W")
psu2 = PSU("PSU", "Corsair V550", 250000, "Corsair", "500W")

# list untuk komponen - komponen yang dipakai dalam merakit PC
Rakit_PC = [[p1, ram1, hdd1, vga1, psu1],[p2, ram2, hdd2, vga2, psu2], [p1, ram2, hdd1, vga2, psu1]]

for i in range(len(Rakit_PC)):
    print(f"-> List Komponen Komputer {i+1}")
    for j in range(len(Rakit_PC[i])):
        print(Komputer.info(Rakit_PC[i][j]))
    print(Komputer.Biaya_Rakit(Rakit_PC[i]))
    print("\n")



