"""
Nama : Rizki Esa Fadillah
NIM    : 121140084
Kelas  : Praktikum PBO - RB

Tugas 3 => Nomor 3
"""

class Handphone:
    # atribut/fungsi kelas
    jumlah_Handphone = 0  # Digunakan untuk menghitung jumlah Handphone

    def __init__(self, merk, Harga, warna):  # Menginisialisasi atribut pada objek
        #atribut public
        self.merk = merk
        # atribut protected
        self._warna = warna
        # atribut private
        self.__Harga = Harga
        Handphone.jumlah_Handphone += 1

    def info_Handphone(self):  # Menampilkan informasi dari Handphone
        print("Merk:", self.merk)
        print("Harga:", self.__Harga)
        print("Warna:", self._warna)

    # method public
    def ubah_merk(self, merk_baru): #mengubah merk dari handphone
        self.merk = merk_baru

    # method protected
    def _ubah_warna(self, warna_baru):  # Mengubah warna dari Handphone
        self._warna = warna_baru

    # method private
    def __ubah_Harga(self, Harga_baru):  # Mengubah Harga Handphone
        self.__Harga = Harga_baru

    def _Tampilkan_Harga(self):
        print("Harga Handphone : ", self.__Harga)

# Inisaslisasi objek dengan atributnya (Variabel Instance)
Handphone1 = Handphone("Samsung", 7500000, "hitam")  
Handphone2 = Handphone("Apple", 20500000, "putih")

# program untuk menggunakan atribut public, protect, dan private
print("Pilih merk ponsel yang akan diubah warna dan harganya : \n1). Samsung \n2). Apple")
# akses atribut/fungsi kelas
print(f"Jumlah Handphone :  {Handphone.jumlah_Handphone}\n")  # Mengakses jumlah dari Handphone
pilih = int(input("Pilih = "))
if pilih == 1:
    # akses atribut public
    print(f"Merk Handphone : {Handphone1.merk}")
    # akses atribut protected
    warna= str(input(f"Warna Handphone saat ini {Handphone1._warna} dibah menjadi warna : "))  # menampilkan Warna Handphone saat ini dan inputan untuk warna baru
    Handphone1._ubah_warna(warna)  # Mengubah warna Handphone menjadi warna sesuai inputan, tidak terjadi erorr karena atribut protect masih dapat diakses oleh class turunannya 
    print(f"Warna Handphone saat ini : {Handphone1._warna}") #menampilkan warna handphone yang baru
    # akses atribut private (Coba akses atribut privat)
    #Handphone1.__ubah_Harga(harga) akan menghasilkan AttributeError karena berada diluar class
    Handphone1._Tampilkan_Harga() 
    # Handphone1._Tampilkan_Harga() bisa digunakan karena methode yang bersifat protect (_Tampilkan_harga) agar dapat diakses oleh class turunannya 
    # dan dalam methode tersebut terdapat atribut privat (__harga) yang telah diakses dalam class handphone sebelumnya sehingga tidak menyebabkan erorr

elif pilih == 2:
    print(f"Merk Handphone : {Handphone2.merk}")
    warna= str(input(f"Warna Handphone saat ini {Handphone2._warna} dibah menjadi warna : "))  
    Handphone2._ubah_warna(warna) 
    print(f"Warna Handphone saat ini : {Handphone2._warna}") 
    Handphone2._Tampilkan_Harga() 


