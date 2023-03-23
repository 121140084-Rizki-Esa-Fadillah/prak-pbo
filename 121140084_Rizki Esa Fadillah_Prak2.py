"""
Nama : Rizki Esa Fadillah
NIM : 121140084
"""

#Baris 7-17, terdapat class dan dialamnya ada methode/fungsi (def) 
class Rizki_Esa_Fadillah:
    #mehode __init__ merupakan methode konstruktor, yang didalamnya terdapat atribut variabel data mahasiswa
    def __init__(self, Nama, Nim, Kelas_PBO_Siakad, Nilai_Matkul, Prodi):
        self. Nama = Nama
        self. Nim = Nim
        self. Kelas_PBO_siakad = Kelas_PBO_Siakad
        self. Nilai_Matkul = Nilai_Matkul
        self. Prodi = Prodi
    #methode print_data, untuk mencetak/mengoutputkan data mahasiswa, dimana data di peroleh dari pemanggilan class pada baris 
    def print_data(self):
        print(f"Data Mahasiswa :\nNama = {self.Nama} \nNIM = {self.Nim}\nProdi = {self.Prodi}\nKelas = {self.Kelas_PBO_siakad}\nNilai = {self.Nilai_Matkul}")
#Baris 18, merupakan sebuah Instance class dengan variabel mahasiswa, dimana setelah pemanggilan class datanya akan di teruskan ke methode konstruktor(__init__)
Mahasiswa = Rizki_Esa_Fadillah("Rizki Esa Fadillah", 121140084, "RB", "A", "Teknik Informatika")
#Baris 20,merupakan proses pemanggilan methode untuk mencetak data 
Mahasiswa.print_data()
