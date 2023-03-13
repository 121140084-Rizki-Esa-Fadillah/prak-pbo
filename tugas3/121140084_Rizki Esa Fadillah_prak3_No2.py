"""
Nama : Rizki Esa Fadillah
NIM    : 121140084
Kelas  : Praktikum PBO - RB

Tugas 3 => Nomor 2
"""
class AkunBank:
    list_pelanggan = []

    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        self.__class__.list_pelanggan.append(self)

    def lihat_menu(self):
        print(f"Selamat datang di Bank Jago \nHalo {self.__nama_pelanggan}, ingin melakukan apa ?")
        print("1. Lihat saldo \n2. Tarik tunai \n3. Transfer saldo \n4. Keluar")
        nomor = int(input("Masukkan nomor input : "))
        if nomor == 1 :
            __class__.lihat_saldo(self)
        elif nomor == 2 :
            __class__.tarik_tunai(self)
        elif nomor == 3:
            __class__.transfer(self)
        elif nomor == 4:
            print("Anda keluar dari program !")
        else :
            print("salah input nomor menu, silakan pilih ulang !\n")
            __class__.lihat_menu(self)

    def lihat_saldo(self):
        print(f"{self.__nama_pelanggan} memiliki saldo {self.__jumlah_saldo}\n")
        __class__.lihat_menu(self)

    def tarik_tunai(self):
        self.nominal = int(input("Masukkan jumlah nominal yang ingin ditarik : "))
        if self.nominal <= self.__jumlah_saldo:
            print("Saldo berhasil di tarik\n")
            self.__jumlah_saldo -= self.nominal
            __class__.lihat_menu(self)
        elif self.nominal > self.__jumlah_saldo:
            print("Nominal saldo yang anda punya tidak cukup\n")
            __class__.tarik_tunai(self)

    def transfer(self):
        self.transfer = int(input("Masukkan nominal yang ingin di transfer : "))
        self.no_tujuan = str(input("Masukkan no rekening tujuan : "))
        for akun in self.__class__.list_pelanggan:
            if self.no_tujuan == akun.__no_pelanggan:
                if self.transfer <= self.__jumlah_saldo:
                    self.__jumlah_saldo -= self.transfer
                    akun.__jumlah_saldo + self.transfer
                    print(f"transfer sebesar Rp. {self.transfer} ke nasabah {akun.__nama_pelanggan} berhasil")
                    __class__.lihat_menu(self)
                else:
                    print("Maaf saldo anda tidak cukup !\n")
                    __class__.transfer(self)
                return    
        print("No Rekening Tujuan tidak dikenal ! kembali ke menu utama\n")
        __class__.lihat_menu(self)

akun1 = AkunBank("1234", "Rizki Esa Fadillah", 5000000000)
akun2 = AkunBank("2345", "Ukraina", 6666666666)
akun3 = AkunBank("3456", "Elon Musk", 9999999999)

print("Pilih Akun Bank : \n1). Akun Rizki Esa Fadillah  \n2). Akun Ukraina \n3). Akun Elon Musk\n")
pilih = int(input("Masukkan Pilihan = "))
if pilih == 1:
    akun1.lihat_menu()
elif pilih == 2:
    akun2.lihat_menu() 
elif pilih == 3:
    akun3.lihat_menu()

