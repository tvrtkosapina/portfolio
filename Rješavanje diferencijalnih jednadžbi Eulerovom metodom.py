import matplotlib.pyplot as plt
from tkinter import *

Rjx = []
Rjy = []
Rj = []

class Diff_jednadzba:
    def __init__(self, diff, x = 0, y = 0, xn = 0, pomak = 0): 
        self.diff = diff
        self.x = x
        self.y = y
        self.xn = xn
        self.pomak = pomak

    def uvrstavanje(self, x, y):
        selfdiff = self.diff
        for i in range(len(selfdiff)):
            if selfdiff[i] == "x":
                if i == 0 and len(selfdiff) > 1:
                    if selfdiff[i+1] == "y":
                        selfdiff = selfdiff.replace(selfdiff[i], "x*")
                elif i == len(selfdiff) - 1:
                    if selfdiff[i-1] == "y":
                        selfdiff = selfdiff.replace(selfdiff[i], "*x")
                else:
                    if selfdiff[i-1] == "y":
                        selfdiff = selfdiff.replace(selfdiff[i], "*x")
                    if selfdiff[i+1] == "y":
                        selfdiff = selfdiff.replace(selfdiff[i], "x*")
        
        selfdiff = selfdiff.replace("^", "**")
        selfdiff = selfdiff.replace("x", str(x))
        selfdiff = selfdiff.replace("y", str(y))
        ddx = float(eval(selfdiff))
        
        return ddx

    def rjesavanje(self, Rjx, Rjy, Rj):
        y0 = self.y
        x0 = self.x
        pomak = self.pomak
        nagib = self.uvrstavanje(x0, y0)
        Rj.append([x0, y0])
        Rjx.append(x0)
        Rjy.append(y0)

        for i in range(0, int(abs(self.xn-self.x)/self.pomak)):
            x0 += pomak
            nagib = self.uvrstavanje(x0, y0)
            y0 += pomak * nagib
            Rj.append([x0, y0])
            Rjx.append(x0)
            Rjy.append(y0)

    def crtanje(Rjx, Rjy):
        plt.plot(Rjx, Rjy)
        plt.xlabel("x-os")
        plt.ylabel("y-os")
        plt.title("Graf")
        plt.show()

prozor = Tk()
prozor.title("Differencijalna jednadžba Eulerovom metodom")

Label(prozor, text='d/dx = ').grid(row=0)
Label(prozor, text='x0 = ').grid(row=1)
Label(prozor, text='y0 = ').grid(row=2)
Label(prozor, text='xn = ').grid(row=3)
Label(prozor, text='pomak(dx)(decimalno pisati s točkom, a ne zarezom) = ').grid(row=4)

e1 = Entry(prozor)  # d/dx
e2 = Entry(prozor)  # x0
e3 = Entry(prozor)  # y0
e4 = Entry(prozor)  # xn
e5 = Entry(prozor)  # pomak

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

def unos():
    diff = e1.get()
    x = float(e2.get())
    y = float(e3.get())
    xn = float(e4.get())
    pomak = float(e5.get())
    diff_jednadzba = Diff_jednadzba(diff, x, y, xn, pomak)
    diff_jednadzba.rjesavanje(Rjx,Rjy,Rj)
    print("yn = ", Rjy[-1])
    print(Rj)
    print("Rjy = ", Rjy)
    print("Rjx = ", Rjx)

def crtanje():
    Diff_jednadzba.crtanje(Rjx,Rjy)

Button(prozor, text='Unos', command=unos).grid(row=5, column=0, sticky=W, pady=4)
Button(prozor, text='Crtaj', command=crtanje).grid(row=5, column=1, sticky=W, pady=4)

mainloop()
