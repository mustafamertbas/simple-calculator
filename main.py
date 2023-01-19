from tkinter import *

def yaz(x):
    s = len(giris.get())
    giris.insert(s,str(x))

hesap = 5
s1 = 0

def islemler(x):
    global hesap
    hesap = x
    global s1
    s1 = float(giris.get())
    print(hesap)
    print(s1)
    giris.delete(0,'end')

s2 = 0
def hesapla():
    global s2
    s2 = float(giris.get())
    print(s2)
    global hesap
    sonuc = 0
    if(hesap==0): sonuc = s1 + s1
    elif(hesap==1):
        sonuc = s1 - s2
    elif(hesap==2):
        sonuc = s1 * s2
    elif(hesap==3):
        sonuc = s1 / s2
    giris.delete(0,'end')
    giris.insert(0,str(sonuc))





pencere = Tk()
pencere.geometry("225x300")
pencere.title("Hesap Makinesi")
pencere.configure(background="#d7d7c1")

giris = Entry(font="Verdana 14 bold",width=14,justify=RIGHT)
giris.place(x=14,y=20)

b =[]


for i in range(1,10):
    b.append(Button(text=str(i),font="Verdana 14 bold",command=lambda x=i:yaz(x)))

sayac = 0

for i in range(0,3):
    for j in range(0,3):
        b[sayac].place(x=20+j*50,y=65+i*50)
        sayac += 1

islem = []

for i in range(0,4):
    islem.append(Button(font="Verdana 14 bold",width=2,command=lambda x=i:islemler(x)))

islem[0]['text'] = "+"
islem[1]['text'] = "-"
islem[2]['text'] = "*"
islem[3]['text'] = "/"

for i in range(0,4):
    islem[i].place(x=170,y=65+50*i)

sb = Button(text=0,font="Verdana 14 bold",command=lambda x=0:yaz(x))
sb.place(x=70,y=214)

nb = Button(text=".",font="Verdana 14 bold",width=2,command=lambda x=".":yaz(x))
nb.place(x=20,y=214)

eb = Button(text="=",fg ="#404040",font="Verdana 14 bold",width=2,command=hesapla)
eb.place(x=120,y=216)

#Made with @mustafamret / @mustafamret.dev
#Bu proje @mustafamret / @mustafamret.dev tarafından yapılmıştır.


pencere.mainloop()
