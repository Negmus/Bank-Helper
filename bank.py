from Tkinter import *
import SendKeys

def wpisz(): #usowanie spacji i wklejanie tekstu
    nr= str(Entry.get(n1))
    nr=nr.replace(" ", "")
    x=nr.isdigit()
    if(x==False):
        check.set("BLAD. Literki w nr.") #dziala/niedziala
        return

    print nr[0:1]

root = Tk()
x= Entry(root)
Label(root, text="Nr konta").grid(row=0, column=0)
n1= Entry(root)
n1.grid(row=0, column=1)
Button(root, text="Wpisuj", command=wpisz).grid(row=0, column=2)
check = StringVar()
Label(root, textvariable=check).grid(row=1, column=1)#Tekst na dole
root.mainloop()
