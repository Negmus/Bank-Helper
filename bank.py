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
    lnr=len(nr)
    if(x==False):
        check.set("Literki w numerze.")  # dziala/niedziala
    elif lnr != 26:
        check.set("Za malo cyfr w numerze.")
        return
    else:
        check.set("Kiknij w pole gdzie chcesz wpisac tekst.")
        global globvar
        globvar = nr
        O = DetectMouseClick()
        O.run()
        print (nr)  # tutaj dam kod od sprawdzania czy lewy klawisz myszy jest wciśnięty
#   pyautogui.click(100, 100);  # Tutaj trzeba będzie dać kod wpisujący numer konta nr
globvar = 0
root = Tk()
x= Entry(root)
Label(root, text="Nr konta:").grid(row=0, column=0)
n1= Entry(root)
n1.grid(row=0, column=2)
Button(root, text="Wpisuj", command=wpisz).grid(row=0, column=4)
check = StringVar()
Label(root, textvariable=check).grid(row=1, column=2)  # Tekst na dole
root.mainloop()
