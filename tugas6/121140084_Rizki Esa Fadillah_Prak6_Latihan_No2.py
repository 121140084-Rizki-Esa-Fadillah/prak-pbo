from abc import ABC, abstractclassmethod

class BDMS(ABC):
    def __init__(self, nama_tabel):
        self.nama_tabel = nama_tabel
    
    @abstractclassmethod
    def lihat_tabel(self):
        pass
    
    @abstractclassmethod
    def tambah_data(self):
        pass

    @abstractclassmethod
    def hapus_tabel(self):
        pass

class MySQL(BDMS):
    def __init__(self, nama_tabel):
        super().__init__(nama_tabel)

    def lihat_tabel(self):
        print(f"SELECT * FROM {self.nama_tabel}")
    
    def tambah_data(self):
        self.nama_kolom = input("Nama kolom : ")
        self.nilai = input("Nilai : ")
        print(f"INSERT INTO {self.nama_tabel} ({self.nama_kolom}) VALUES ({self.nilai})")
    
    def hapus_tabel(self):
        print(f"DROP TABLE {self.nama_tabel}")
    
class MangoDB(BDMS):
    def __init__(self, nama_tabel):
        super().__init__(nama_tabel)

    def lihat_tabel(self):
        print (f"db.{self.nama_tabel}.find()")
    
    def tambah_data(self):
        self.nama_kolom = input("Nama kolom : ")
        self.nilai = input("Nilai : ")
        print(f"db.{self.nama_tabel}.insertOne({self.nama_kolom}:{self.nilai})")
    
    def hapus_tabel(self):
        print(f"db.{self.nama_tabel}.drop()")
    
Database1 = MySQL("Produk")
Database2 = MangoDB("Pembeli")

Menu = True
print("Pilih server database : \n1). MySQL \n2). MongoDB")
pilih = input("Pilih = ")

if pilih == "1":
    server = Database1
elif pilih == "2":
    server = Database2
else:
    print("Inputan anda tidak termasuk dalam pilihan !")

while (Menu == True):
    print("\nAktivitas yang di sediakan oleh masing-masing server database : \n1). Lihat tabel \n2). Tambah data \n3). Hapus tabel\n4). Keluar server")
    Aktivitas = int(input("Pilih = "))
    if Aktivitas == 1:
        server.lihat_tabel()
    elif Aktivitas == 2:
        server.tambah_data()    
    elif Aktivitas == 3:
        server.hapus_tabel()
    elif Aktivitas == 4:
        Menu = False
    else:
        print("Fasilitas tak tersedia !!")
print("~~~Server Ditutup~~~")