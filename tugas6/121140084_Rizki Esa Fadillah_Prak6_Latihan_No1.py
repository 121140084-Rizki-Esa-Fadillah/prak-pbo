from abc import ABC, abstractclassmethod

class AkunBank(ABC):
    def __init__(self, nama, tahun_daftar, saldo):
        self. nama = nama
        self. tahun_daftar = tahun_daftar
        self. saldo =saldo

    @abstractclassmethod
    def transfer(self):
        pass

    @abstractclassmethod
    def lihat_suku_bunga(self):
        pass

    def lihat_saldo(self):
        print(f"Jumlah saldo pelanggan {self.nama} adalah sebesar Rp.{self.saldo}")
    
class AkunGold(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super(). __init__(nama, tahun_daftar, saldo)

    def transfer(self):
        self.transfer = int(input("Masukkan nominal transfer : "))
        if self.transfer >= 100000:
            if (2023 - self.tahun_daftar) >= 3:
                self.transfer += 0
            elif (2023 - self.tahun_daftar) < 3:
                self.transfer += 2000
        else:
            self.transfer += 0
        print(f"Transfer sebesara Rp.{self.transfer} Berhasil")
        self.saldo -= self.transfer 

    def lihat_suku_bunga(self):
        if self.saldo >= 1000000000:
            if (2023 - self.tahun_daftar) >= 3:
                print(f"Jumlah suku bunga yang diperoleh {self.nama} adalah sebesar Rp.{float(self.saldo*0.01)}")
            elif (2023 - self.tahun_daftar) < 3:
                print(f"Jumlah suku bunga yang diperoleh {self.nama} adalah sebesar Rp.{float(self.saldo*0.02)}")
        else:
            print(f"Jumlah suku bunga yang diperoleh {self.nama} adalah sebesar Rp.{float(self.saldo*0.03)}")

class AkunSilver(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super(). __init__(nama, tahun_daftar, saldo)

    def transfer(self):
        self.transfer = int(input("Masukkan nominal transfer : "))
        if self.transfer >= 100000:
            if (2023 - self.tahun_daftar) >= 3:
                self.transfer += 2000
            elif (2023 - self.tahun_daftar) < 3:
                self.transfer += 5000
        else:
            self.transfer += 0
        print(f"Transfer sebesara Rp.{self.transfer} Berhasil")
        self.saldo -= self.transfer 

    def lihat_suku_bunga(self):
        if self.saldo >= 10000000:
            if (2023 - self.tahun_daftar) >= 3:
                print(f"Jumlah suku bunga yang diperoleh {self.nama} adalah sebesar Rp.{float(self.saldo*0.01)}")
            elif (2023 - self.tahun_daftar) < 3:
                print(f"Jumlah suku bunga yang diperoleh {self.nama} adalah sebesar Rp.{float(self.saldo*0.02)}")
        else:
            print(f"Jumlah suku bunga yang diperoleh {self.nama} adalah sebesar Rp.{float(self.saldo*0.03)}")

Pelanggan1 = AkunGold("Rizki", 2021, 1500000000)
Pelanggan2 = AkunSilver("Esa", 2016, 25000000)

login = True
print("Akun bank : \n1). Akun Gold \n2). Akun Silver")
Pilih = int(input("Pilih akun = "))

if Pilih == 1:
    akun = Pelanggan1
elif Pilih == 2:
    akun = Pelanggan2
else:
    print("Maaf inputan anda salah !!!")

while (login == True):
    print("\nFasilitas yang di sediakan oleh Bank : \n1). Lihat saldo \n2). Transfer \n3). Lihat suku bunga \n4). Keluar Aplikasi")
    Fasilitas = int(input("Pilih = "))
    if Fasilitas == 1:
        akun.lihat_saldo()
    elif Fasilitas == 2:
        akun.transfer()
    elif Fasilitas == 3:
        akun.lihat_suku_bunga()
    elif Fasilitas == 4:
        login = False
    else:
        print("Fasilitas tak tersedia !!")
print("Terimakasih atas kepercayaanya ($~$)")



        