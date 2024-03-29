"""
Nama : Rizki Esa Fadillah
NIM : 121140084
Buatlah program yang dapat menerima inputan username dan pasword dari user sebanyak 3 kali.
Jika percobaan oleh user kurang dari sama dengan 3 kali, maka berhasil login, jika lebih dari 3 kali
maka akun diblokir. Dengan username yang digunakan adalah sebagai berikut :
=> username     = informatika
=> password     = 12345678
"""
#Baris ke 11 - 12 berisi variabel login (untuk parameter boolean pada while) dan i (untuk memberikan nilai awal pada kode program menetukan kesempatan login)
login = False
i = 1
#Baris ke 14 - 15 berisi outputkan yang digunakan sebagai instruksi ke pengguna bahwa hanya memiliki kesempatan login 3x
print("Masukkan username dan password dengan tepat !!!")
print("Sisa percobaan : 3 kali")
#Baris 17 - 31, terdapat perulangan while untuk membuat program login
while (i <= 3):
    #Baris 20 - 22, membuat variabel username (str) dan password (int) dengan nilai dari user. 
    #Kemudian nilai variabel i akan bertambah 1 setiap perulangan while, kemudian melanjutkan ke kode berikutnya
    username = str(input("\nUsername = "))
    password = int(input("Password = "))
    i += 1
    #Baris 25 - 31, terdapat percabangan if - else untuk mengecek apakah username dan pasword yang digunakan sesuai ketentuan atau tidak
        #Jika if benar, maka variabel boolean login berubah nilai menjadi True, dan mengganti variabel i menjadi 4 agar perulangan while berhenti dan melanjutkan program ke baris 34
    if username == "informatika" and password == 12345678:
        login = True
        i = 4
        # percabangan else, akan menginfokan ke user jika inputan kurang tepat, dan mengingatkan jumlah kesempatan login
    else:
        print("\nMaaf username atau password yang anda masukkan masih kurnag tepat !!!")
        print("Sisa percobaan : " + str(4 - i) + " kali")
#Baris 34 - 38, berisi percabangan if - else untuk menetukan hasil akhir inputan 
    #Jika if benar, maka login berhasil
if login == True:
    print("\nSelamat anda berhasil login :)")
    #jika elif benar, maka login gagal dalam 3x kesempatan dan akun akan diblokir
elif login == False:
    print("Maaf akun anda saya blokir :(")
