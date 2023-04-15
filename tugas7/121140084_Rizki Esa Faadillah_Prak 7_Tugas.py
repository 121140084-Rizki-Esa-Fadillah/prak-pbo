from tkinter import *
import math

window = Tk()
window.title("Kalkulator GUI Dengan Python")
window.geometry('500x200')

lbl = Label(window, text="Masukan Nilai Pertama : ",anchor="e",width=20)
lbl.grid(column=0, row=0)
nilai1 = Entry(window, width=30)  
nilai1.grid(column=1, row=0, columnspan=1)  

lbl2 = Label(window, text="Masukan Nilai Kedua : ",anchor="e",width=20)
lbl2.grid(column=0, row=1)
nilai2 = Entry(window, width=30)  
nilai2.grid(column=1,row=1, columnspan=1)  

lbl3 = Label(window, text="Hasilnya adalah : ",anchor="e",width=20)
lbl3.grid(column=0, row=6)

hasil = Label(window, text="0",anchor="w",width=30)
hasil.grid(column=1, row=6, columnspan=2)

def tambah():
    hasil.configure(text=(int(nilai1.get())+int(nilai2.get())))
    
def kurang():
    hasil.configure(text=(int(nilai1.get())-int(nilai2.get()))) 
    
def kali():
    hasil.configure(text=(int(nilai1.get())*int(nilai2.get())))
    
def bagi():
    try:
        hasil.configure(text=(int(nilai1.get())/int(nilai2.get())))
    except ZeroDivisionError:
        hasil.configure(text="Tidak dapat dibagi dengan nol")

def akar():
    try:
        hasil.configure(text=math.sqrt(int(nilai1.get())))
    except ValueError:
        hasil.configure(text="Masukan nilai yang valid")

def pangkat():
    hasil.configure(text=(int(nilai1.get())**int(nilai2.get())))

def selesai():
    window.destroy()

btnTambah = Button(window, text="Tambah", width=10, command=tambah)
btnTambah.grid(column=0, row=3, padx=5, pady=5)

btnKurang = Button(window, text="Kurang", width=10, command=kurang)
btnKurang.grid(column=1, row=3, padx=5, pady=5)

btnKali = Button(window, text="Kali", width=10, command=kali)
btnKali.grid(column=0, row=4, padx=5, pady=5)  

btnBagi = Button(window, text="Bagi", width=10, command=bagi)
btnBagi.grid(column=1, row=4, padx=5, pady=5)  

btnAkar = Button(window, text="Akar", width=10, command=akar)
btnAkar.grid(column=2, row=3, padx=5, pady=5)

btnPangkat = Button(window, text="Pangkat", width=10, command=pangkat)
btnPangkat.grid(column=2, row=4, padx=5, pady=5)

btnSelesai = Button(window, text="Selesai", width=10, command=selesai)
btnSelesai.grid(column=1, row=7, padx=5, pady=5)

window.mainloop()
