from tkinter import *
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

pencere = Tk()
pencere.geometry("900x600+150+50")
pencere.title("Fotoğraf Albümü")
pencere.configure(background="blue")
hosgeldin = Label(text="\n\n\t\t Fotoğraf Albümüne Hoşgeldin! \t\t\n\n", font="Times 18 bold",
                  fg="black", bg="blue")
hosgeldin.pack()
mainloop()

fotograflar =["Renklipapatya.jpg","papatyaBöcek.jpg","papatya"]
