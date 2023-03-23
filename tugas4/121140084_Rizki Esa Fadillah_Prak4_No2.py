"""
Nama : Rizki Esa Fadillah
NIM    : 121140084
Kelas  : Praktikum PBO - RB

Tugas 4 => Nomor 1

=== ~ Inheritance dan polymorphism ~ ==
"""
class Robot:
    jumlah_turn = 0

    def __init__(self, nama = "", health = 0, demage = 0):
        self.nama = nama
        self.health = health
        self.damage = demage
        
        
    def __sub__(self,other):
        self.health -= other.damage
        return self.health
        
    def __str__(self):
        return f"({self.nama}) menyerang sebanyak {self.damage} DMG dan sudah menang sebanyak : "
    
    def lakukan_aksi(self,other):
        other.health -= self.damage
        return other.health
    
class Antares(Robot):
    def __init__(self):
        self.nama = "Antares"
        self.health = 50000
        self.damage = 5000
    
    def lakukan_aksi(self,other,turn):
        if turn % 3 == 0:
            self.damage *= 1.5
        elif turn % 3 == 1 and turn > 3:
            self.damage = 5000
        Robot.lakukan_aksi(self,other)
     
class Alphasetia(Robot):
    def __init__(self):
        self.nama = "Alphasetia"
        self.health = 40000
        self.damage = 6000
    
    def lakukan_aksi(self, other, turn):
        if turn % 2 == 0:
            self.health += 4000
        Robot.lakukan_aksi(self,other)
        
class Lecalicus(Robot):
    def __init__(self):
        self.nama = "Lecalicus"
        self.health = 45000
        self.damage = 5500
    
    def lakukan_aksi(self,other,turn):
        if turn % 4 == 0:
            self.health += 7000
            self.damage *= 2
        elif turn % 4 == 1 and turn > 4:
            self.damage = 5500
        Robot.lakukan_aksi(self, other)
   
print("selamat datang di pertandingan robot Yamako")
robot = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
if robot == 1:
    robotmu = Antares()
elif robot == 2:
    robotmu = Alphasetia()
elif robot == 3:
    robotmu = Lecalicus()
    
robot = int(input("Pilih robot lawan(1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
if robot == 1:
    robot_lawan = Antares()
elif robot == 2:
    robot_lawan = Alphasetia()
elif robot == 3:
    robot_lawan = Lecalicus()
    
print("\nPilih : \n1 = Batu \n2 = kertas \n3 = gunting\n")
turn = 1
menangmu = 0
menang_lawan = 0

while(True):
    print(f"Turn saat ini : {turn}")
    print(f"Health robotmu ({robotmu.nama} - {robotmu.health} HP), health robot lawan ({robot_lawan.nama} - {robot_lawan.health} HP)")
    tanganmu = int(input("Pilih tangan robotmu : "))
    tangan_lawan = int(input("Pilih tangan robot lawan : "))
        
    # Jika robotmu menang
    if (tanganmu == 1 and tangan_lawan == 3) or (tanganmu == 2 and tangan_lawan == 1) or (tanganmu == 3 and tangan_lawan == 2):
        menangmu += 1
        robotmu.lakukan_aksi(robot_lawan, menangmu)
        print("Robotmu", robotmu.__str__(), menangmu)
        
    # Jika robot lawan menang
    elif (tanganmu == 1 and tangan_lawan == 2) or (tanganmu == 2 and tangan_lawan == 3) or (tanganmu == 3 and tangan_lawan == 1):
        menang_lawan += 1
        robot_lawan.lakukan_aksi(robotmu,menang_lawan)
        print("Robot lawan", robot_lawan.__str__(), menang_lawan)
        
    elif (tanganmu == 1 and tangan_lawan == 1) or (tanganmu == 2 and tangan_lawan == 2) or (tanganmu == 3 and tangan_lawan == 3):
        print("Hasil Seri, melakukan tanding ulang")
    
    elif (tanganmu != 1 and tangan_lawan != 1) or (tanganmu != 2 and tangan_lawan != 2) or (tanganmu != 3 and tangan_lawan != 3):
        print("Tidak termasuk ke dalam pilihan kertas, batu, atau guntung, silakan tanding ulang")
    print("\n")
    
    if robotmu.health <= 0 or robot_lawan.health <= 0:
        print(f"Jumlah turn yang dilakukan : {turn}")
        if robotmu.health > robot_lawan.health:
            print(f"Robot lawan ({robot_lawan.nama}) telah mati = 0 HP")
            print(f"Pemenang di pertandingan robot Yamako adalah robotmu ({robotmu.nama})")
        else:
            print(f"Robotmu ({robotmu.nama}) telah mati = 0 HP")
            print(f"Pemenang di pertandingan robot Yamako adalah robot lawan ({robot_lawan.nama})")
        break  
    turn += 1