from tkinter import *
import pyautogui
from pymouse import PyMouseEvent
import sys



class DetectMouseClick(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)
    def click(self, x, y, button, press):
        if button == 1:
            if press:
                print("click")
                pyautogui.typewrite(globvar)
                self.do = 1
            else:
                self.do = 0
                sys.exit("Koniec")
        else:
            self.do = 0
            sys.exit("Koniec")


def wpisz():  # usowanie spacji i wklejanie tekstu
    nr= str(Entry.get(n1))
    nr=nr.replace(" ", "")
    x=nr.isdigit()
    if(x==False):
        check.set("BLAD. Literki w nr.")  # dziala/niedziala
        return
    else:
        global globvar
        globvar = nr
        O = DetectMouseClick()
        O.run()
        print (nr)  # tutaj dam kod od sprawdzania czy lewy klawisz myszy jest wciśnięty
#   pyautogui.click(100, 100);  # Tutaj trzeba będzie dać kod wpisujący numer konta nr
globvar = 0
root = Tk()
x= Entry(root)
Label(root, text="Nr konta").grid(row=0, column=0)
n1= Entry(root)
n1.grid(row=0, column=1)
Button(root, text="Wpisuj", command=wpisz).grid(row=0, column=2)
check = StringVar()
Label(root, textvariable=check).grid(row=1, column=1)  # Tekst na dole
root.mainloop()
