from tkinter import *
from math import *
import tkinter.messagebox

global islem
islem=["+", "-", "*", "/"]
global s
s=0
global s1
s1=0
global s2
s2=0
global hesaplama
hesaplama=0

def ekranisil():
    ekran.delete(0,"end")

def yaz(x):
    s = len(degisken.get())
    if(s <= 20):
        ekran.insert(s, str(x))
    else:
        tkinter.messagebox.showerror("KARAKTER SINIRI","Daha fazla karakter giremezsiniz!!")

def piyaz(x):
    s = len(degisken.get())
    global olasiliklar
    olasiliklar=["3.141592","2.718281","3.141592+3.141592","3.141592**3.141592"]
    olasilikler2=["2.718281**2.718281", "2.718281**3.141592","3.141592**2.718281"]
    if (s <= 20):
        if (ekran.get() in olasiliklar and degisken.get() in olasilikler2):
            ekran.insert(s, str(x))

    else:
        tkinter.messagebox.showerror("KARAKTER SINIRI", "Daha fazla karakter giremezsiniz!!")

def eyaz(x):
    s = len(degisken.get())
    if (s <= 20):
        if (ekran.get() != "2.718281"and ekran.get() != "3.141592" and ekran.get() != "2.718281+2.718281" and ekran.get() != "2.718281**2.718281" and degisken.get() != "3.141592**3.141592" and ekran.get() != "2.718281**3.141592" and degisken.get() != "3.141592**2.718281"):
            ekran.insert(s, str(x))
    else:
        tkinter.messagebox.showerror("KARAKTER SINIRI", "Daha fazla karakter giremezsiniz!!")

def silecek():
    uzunluk = len(degisken.get())
    ekran.delete(uzunluk-1,"end")

def faktoriyelal():
    s1 = str(degisken.get())

    if (len(s1) == 0):
        tkinter.messagebox.showwarning("HATA", "Lütfen sayı girin!")
    else:
        if ("." in s1):
            tkinter.messagebox.showerror("HATA", "Tam sayı girin!")
        else:
            s1 = eval(s1)
            c = factorial(int(s1))
            ekran.delete(0,"end")
            ekran.insert(0,int(c))

def karekokal():
    s1 = str(degisken.get())

    if (len(s1) == 0):
        tkinter.messagebox.showwarning("HATA", "Lütfen sayı girin!")
    else:
        if ("." in s1):
            tkinter.messagebox.showerror("HATA", "Tam sayı girin!")
        else:
            a = pow(int(s1), 0.5)
            ekran.delete(0, "end")
            if(a % 2 == 0 or a % 2 == 1):
                ekran.insert(0,int(a))
            else:
                ekran.insert(0, float(a))

def karesinial():
    s1 = str(degisken.get())
    if (len(s1) == 0):
        tkinter.messagebox.showwarning("HATA", "Lütfen sayı girin!")
    else:
        a = pow(float(s1),2)
        ekran.delete(0, "end")
        if (a % 2 == 0 or a % 2 == 1):
            ekran.insert(0, int(a))
        else:
            ekran.insert(0,float(a))

def kupunual():
    s1 = str(degisken.get())
    if (len(s1) == 0):
        tkinter.messagebox.showwarning("HATA", "Lütfen sayı girin!")
    else:
        a = pow(float(s1),3)
        ekran.delete(0, "end")
        if (a % 2 == 0 or a % 2 == 1):
            ekran.insert(0,int(a))
        else:
            ekran.insert(0,float(a))

def ussunual():
    s = len(ekran.get())
    s1 = str(ekran.get())

    if (len(s1) == 0):
        tkinter.messagebox.showwarning("HATA", "Lütfen sayı girin!")
    else:
        s1 = ekran.get()
        if(s1[s-1] != "*"):
            ekran.insert(s,"**")

def birboluf():
    s1 = str(ekran.get())
    if (len(s1) == 0):
        tkinter.messagebox.showwarning("HATA", "Lütfen sayı girin!")
    else:
        hesap = 1/float(s1)
        ekranisil()
        if (hesap % 2 == 0 or hesap % 2 == 1):
            ekran.insert(0,int(hesap))
        else:
            ekran.insert(s,float(hesap))

def logal():
    ekranisil()
    ekran.insert(0,"log(")

def radcevir():
    s1 = str(ekran.get())
    if (len(s1) == 0):
        tkinter.messagebox.showwarning("HATA", "Lütfen sayı girin!")
    else:
        hesap = radians(float(s1))
        ekranisil()
        ekran.insert(0, hesap)

def sinal():
    ekranisil()
    ekran.insert(0, "sin(")

def cosal():
    ekranisil()
    ekran.insert(0, "cos(")

def tanal():
    ekranisil()
    ekran.insert(0, "tan(")

def cotal():
    ekranisil()
    ekran.insert(0, "cot(")

def ilk(x):

    global hesap
    hesap = x
    s = len(degisken.get())
    s1 = degisken.get()

    if(islem[0] == s1[s-1]):
        ekran.delete(s-1,"end")
        ekran.insert(s,hesap)
    elif(islem[1] == s1[s-1]):
        ekran.delete(s - 1, "end")
        ekran.insert(s, hesap)
    elif(islem[2] == s1[s-1]):
        ekran.delete(s - 1, "end")
        ekran.insert(s, hesap)
    elif(islem[3] == s1[s-1]):
        ekran.delete(s - 1, "end")
        ekran.insert(s, hesap)
    else:
        ekran.insert(s,x)
        s+=1

def hesapla():
    s2 = str(degisken.get())
    s = len(degisken.get())
    global hesaplama
    hesaplama = 0

    if(s2[s-1] in islem):
        ekran.delete(s+1,"end")
        s2 = str(degisken.get())
        ekranisil()
        hesaplama = eval(s2)

        if (hesaplama % 2 == 0):
            ekran.insert(0, int(hesaplama))
        else:
            ekran.insert(0, hesaplama)
    else:
        ekranisil()
        if(s2[0:3] != "cot"):
            hesaplama = eval(s2)
        if(hesaplama % 2 == 0):
            ekran.insert(0,int(hesaplama))
        else:
            ekran.insert(0, hesaplama)
        if ("log" == s2[0:3]):
            ekranisil()
            bak = log(int(s2[4:s - 1]), 10)
            if (bak % 2 == 0 or bak % 2 == 1):
                ekran.insert(0, int(bak))
            else:
                ekran.insert(0, float(bak))
        if ("sin" == s2[0:3]):
            ekranisil()
            bak = sin(radians(int(s2[4:s - 1])))
            if (bak % 2 == 0 or bak % 2 == 1):
                ekran.insert(0, int(bak))
            else:
                if ( bak == 1.2246467991473532e-16 or bak == -2.4492935982947064e-16 or bak == 3.6739403974420594e-16 or bak == -4.898587196589413e-16):
                    ekranisil()
                    ekran.insert(0, "0")
                ekran.insert(0, float(bak))
        if ("cos" == s2[0:3]):
            ekranisil()
            bak = cos(radians(int(s2[4:s - 1])))
            if (bak % 2 == 0 or bak % 2 == 1):
                ekran.insert(0, int(bak))
            else:
                if (bak == 6.123233995736766e-17 or bak == -1.8369701987210297e-16 or bak == 3.061616997868383e-16 or bak == -4.286263797015736e-16):
                    ekranisil()
                    ekran.insert(0, "0")
                ekran.insert(0, float(bak))
        if ("tan" == s2[0:3]):
            ekranisil()
            bak = tan(radians(int(s2[4:s - 1])))
            if (bak % 2 == 0 or bak % 2 == 1):
                ekran.insert(0, int(bak))
            else:
                ekran.insert(0, float(bak))
            if (bak == 16331239353195370):
                ekranisil()
                tkinter.messagebox.showerror("HATA", "0'a bölünme hatası!")
            if(bak == -1.2246467991473532e-16 or bak == -2.4492935982947064e-16 or bak == -3.6739403974420594e-16 or bak == -4.898587196589413e-16):
                ekranisil()
                ekran.insert(0,"0")
        try:
            if ("cot" == s2[0:3]):
                ekranisil()
                sonuc = float(tan(radians(int(s2[4:s - 1]))))
                bak = 1/float(sonuc)
                if (bak % 2 == 0 or bak % 2 == 1):
                    ekran.insert(0, int(bak))
                else:
                    ekran.insert(0, float(bak))
                if(bak == 6.123233995736766e-17 or bak == 1.83697019872103e-16 or bak == 3.061616997868383e-16 or bak == 4.2862637970157356e-16):
                    ekranisil()
                    ekran.insert(0,"0")
        except(ZeroDivisionError):
            tkinter.messagebox.showerror("HATA","0'a bölünme hatası!")

def standart():
    #pencere olusturma

    global pencere
    pencere = Tk()
    pencere.title("HESAP MAKİNESİ")
    pencere.geometry("340x352")
    pencere.config(background="black")

    #ekran olusturma
    global ekran
    global degisken
    degisken = StringVar()
    ekran = Entry(justify=RIGHT,width=28,textvariable=degisken,font=("NEW TIMES ROMAN",15),fg="black",bg="white",insertbackground="black")

    #buton olusturma
    global buton_listesi
    buton_listesi = list()

    for i in range(1,10):
        buton_listesi.append(Button(pencere,text=str(i),width=4,height=2,font=("new times roman",10),fg="black",bg="white",command=lambda x=i:yaz(x)))

    usal = Button(pencere,text="xʸ",width=3,height=0,font=("new times roman", 14), fg="black", bg="turquoise",command=ussunual)

    foto = PhotoImage(file="silme.png")
    silme = Button(pencere,image=foto,height=0,bg="white",command=silecek)

    sb = Button(pencere,text="0",width=10,height=2,font=("new times roman",10),command=lambda x=0:yaz(x))

    nokta = Button(pencere,text=".",width=3,font=("new times roman",15),command=lambda x=".":yaz(x))

    sifirlama = Button(pencere,text="C",width=3,height=0,font=("new times roman",16),fg="black",bg="brown",command=ekranisil)

    pisayisi = Button(pencere,text="π",width=3,font=("new times roman",15),fg="black",bg="turquoise",command=lambda x="3.141592":piyaz(x))

    esayisi = Button(pencere,text="e",width=3,font=("new times roman",15),fg="black",bg="turquoise",command=lambda x="2.718281":eyaz(x))

    birbolu = Button(pencere,text="1/x",width=3,font=("new times roman",15),fg="black",bg="turquoise",command=birboluf)

    logaritma = Button(pencere,text="log",width=3,font=("new times roman",15),fg="black",bg="turquoise",command=logal)

    radyan = Button(pencere, text="RAD", width=3, font=("new times roman", 15), fg="black", bg="turquoise",command=radcevir)

    sinus = Button(pencere,text="sin",width=3,font=("new times roman",15),fg="black",bg="turquoise",command=sinal)

    cosinus = Button(pencere,text="cos",width=3,font=("new times roman",15),fg="black",bg="turquoise",command=cosal)

    tanjant = Button(pencere,text="tan",width=3,font=("new times roman",15),fg="black",bg="turquoise",command=tanal)

    cotanjant = Button(pencere,text="cot",width=3,font=("new times roman",15),fg="black",bg="turquoise",command=cotal)

    ilkparantez = Button(pencere,text="(",width=3,font=("new times roman",15),fg="black",bg="turquoise",command=lambda x="(":yaz(x))

    ikinciparantez = Button(pencere,text=")",width=3,font=("new times roman",15),fg="black",bg="turquoise",command=lambda x=")":yaz(x))

    topla = Button(pencere,text="+",width=3,height=0,font=("new times roman",16),fg="black",bg="blue",command=lambda x="+":ilk(x))
    cikar = Button(pencere,text="-",width=3,height=1,font=("new times roman",16),fg="black",bg="blue",command=lambda x="-":ilk(x))
    carp = Button(pencere,text="*",width=3,height=0,font=("new times roman",16),fg="black",bg="blue",command=lambda x="*":ilk(x))
    bol = Button(pencere,text="/",width=3,height=0,font=("new times roman",16),fg="black",bg="blue",command=lambda x="/":ilk(x))
    esittir = Button(pencere,text="=",width=3,height=3,font=("new times roman",16),fg="red",bg="light green",command=hesapla)
    kareal = Button(pencere,text="x²",width=3,height=0,font=("new times roman",14),fg="black",bg="turquoise",command=karesinial)
    kupal = Button(pencere,text="x³",width=3,height=0,font=("new times roman",14),fg="black",bg="turquoise",command=kupunual)
    faktoriyel = Button(pencere,text="!",width=3,height=0,font=("new times roman",14),fg="black",bg="turquoise",command=faktoriyelal)
    karekok = Button(pencere, text="√¯", width=3, height=0, font=("new times roman", 14), fg="black", bg="turquoise",command=karekokal)

    #buton ve entry yerlestirme

    ekran.place(x=15,y=15)

    sayac=6
    for i in range(0,3):
        buton_listesi[sayac].place(x=70+i*50,y=150)
        sayac+=1

    sayac=3
    for i in range(0,3):
        buton_listesi[sayac].place(x=70+i*50,y=200)
        sayac+=1

    sayac=0
    for i in range(0,3):
        buton_listesi[sayac].place(x=70+i*50,y=250)
        sayac+=1

    sb.place(x=70,y=299)

    nokta.place(x=168,y=302)

    sifirlama.place(x=220,y=151)

    silme.place(x=273,y=152)

    topla.place(x=220,y=300)

    cikar.place(x=220,y=251)

    carp.place(x=220,y=202)

    bol.place(x=272,y=202)

    esittir.place(x=272,y=252)

    kareal.place(x=70,y=102)

    kupal.place(x=120,y=102)

    faktoriyel.place(x=222,y=102)

    usal.place(x=170, y=102)

    karekok.place(x=274, y=102)

    pisayisi.place(x=20,y=302)

    esayisi.place(x=20,y=252)

    birbolu.place(x=20,y=202)

    logaritma.place(x=20,y=152)

    radyan.place(x=20, y=102)

    sinus.place(x=20,y=52)

    cosinus.place(x=70,y=52)

    tanjant.place(x=120,y=52)

    cotanjant.place(x=170,y=52)

    ilkparantez.place(x=222,y=52)

    ikinciparantez.place(x=274,y=52)

    pencere.mainloop()


standart()

#kod sonu :)) oh beeee :))


