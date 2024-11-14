#Mengambil dan Menampilkan Data (Part 2)

from tkinter import *
import tkinter.messagebox

class DataInOut:
    def __init__(self, root):
        self.root = root
        self.root.title('Penjumlahan')
        self.root.geometry('400x200+0+0')
        frame1 = Frame(self.root)
        frame1.grid()
        frame2 = Frame(frame1)
        frame2.grid(row=0, column=0)
        frame2 = Frame(frame1)
        frame2.grid(row=1, column=0)
        frame3 = Frame(frame1)
        frame3.grid(row=2, column=0)

        FirstNum = StringVar()
        SecondNum = StringVar()
        Hasil = StringVar()

        self.lblFirstNum = Label(frame2, text="Masukkan bilangan pertama")
        self.lblFirstNum.grid(row=0, column=0)
        self.txtFirstNum = Entry(frame2, textvariable=FirstNum)
        self.txtFirstNum.grid(row=0, column=1)
        self.lblSecondNum = Label(frame2, text="Masukkan bilangan kedua")
        self.lblSecondNum.grid(row=1, column=0)
        self.txtSecondNum = Entry(frame2, textvariable=SecondNum)
        self.txtSecondNum.grid(row=1, column=1)

        self.lblHasil = Label(frame2, text="Hasil")
        self.lblHasil.grid(row=2, column=0)
        self.txtHasil = Entry(frame2, textvariable=Hasil)
        self.txtHasil.grid(row=2, column=1)

        def jumlah():
            num1 = float(self.txtFirstNum.get())
            num2 = float(self.txtSecondNum.get())
            jumlah = num1 + num2
            Hasil.set(jumlah)

        self.btnHitung = Button(frame3, text='Jumlahkan', command=jumlah)
        self.btnHitung.grid(row=0, column=0)

        def reset():
            self.txtFirstNum.delete(0, END)
            self.txtSecondNum.delete(0, END)
            self.txtHasil.delete(0, END)

        self.btnReset = Button(frame3, text='Reset', command=reset)
        self.btnReset.grid(row=0, column=1)

        def exit():
            self.root.destroy()

        self.btnExit = Button(frame3, text='Exit', command=exit)
        self.btnExit.grid(row=0, column=2)
        
root = Tk()
app = DataInOut(root)
root.mainloop()