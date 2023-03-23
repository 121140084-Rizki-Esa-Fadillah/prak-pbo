"""
Nama : Rizki Esa Fadillah
NIM : 121140084
Buatlah program yang dapat menerima n input bilangan integer dari user kemudian menghasilakan output kotak * dengan panjang n dan lebar n
"""

#Baris 8, untuk membuat variabel (n) dengan nilai inputan dari user, untuk menentukan panjang dan lebar kotak
n = int(input("Masukkan nilai n = "))
#Baris 11 - 14, menggunakan perulangan bersarang untuk meng-outputkan karakter *  hingga membentuk kotak
#for baris 11 akan mengerjakan output lebar kotak, for baris 12 akan mengerjakan output panjang kotak
for i in range(0, n):
    for k in range(0, n):
        print("*", end="")
    print("")
            

