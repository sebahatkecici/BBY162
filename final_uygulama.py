import tkinter
from random import choice


class Simon() :
    def __init__(self, anaSayfa):
        self.anaSayfa = anaSayfa
        self.anaSayfa.minsize(640, 480)
        self.anaSayfa.resizable(False, False)
        self.anaSayfa.title("Simon Oyunu")
        self.anaSayfa.update()
        self.canvas = tkinter.Canvas(self.anaSayfa,width=self.anaSayfa.winfo_width(),height=self.anaSayfa.winfo_height())
        self.canvas.pack()

        self.renk = ("red", "blue", "dark green", "yellow")
        self.acıkRenk = ("pink", "light blue", "light green", "white")
        self.parlayanRenk = [color for color in self.renk]
        self.dikdortgenler = []

        self.sıra = [choice(self.renk)]
        self.sırası = 0
        self.draw_canvas()
        self.sırasınıGoster()

        self.anaSayfa.mainloop()

    def sırasınıGoster(self):
        self.yak(self.sıra[self.sırası])
        if(self.sırası < len(self.sıra) - 1):
            self.sırası += 1
            self.anaSayfa.after(1000, self.sırasınıGoster)
        else :
            self.sırası = 0

    def yak(self, color):
        index = self.renk.index(color)
        if self.parlayanRenk[index] == self.renk[index] :
            self.parlayanRenk[index] = self.acıkRenk[index]
            self.anaSayfa.after(1000, self.yak, color)
        else :
            self.parlayanRenk[index] = self.renk[index]
        self.draw_canvas()


    def check_choice(self):
        dikdortgen = self.canvas.find_withtag("current")[0]
        Dikdortgen = self.dikdortgenler.index(dikdortgen)
        renk= self.renk[Dikdortgen]
        if renk == self.sıra[self.sırası]:
            if self.sırası < len(self.sıra) - 1:
                self.sırası += 1
            else :
                self.anaSayfa.title("Simon Oyunu - Puanınız: {}".format(len(self.sıra)))
                self.sıra.append(choice(self.renk))
                self.sırası = 0
                self.sırasınıGoster()
        else :
            self.anaSayfa.title("Simon oyununu  Kaybettiniz! | Puanınız: {}".format(len(self.sıra)))
            self.sıra[:] = []
            self.sıra.append(choice(self.renk))
            self.sırası = 0
            self.sırasınıGoster()


    def draw_canvas(self):
        self.dikdortgenler[:] = []
        self.canvas.delete("all")
        for index, color in enumerate(self.parlayanRenk):
            if index <= 1:
                rectangle = self.canvas.create_rectangle(
                                          index * self.anaSayfa.winfo_width(),
                                          0, self.anaSayfa.winfo_width() / 2,
                                          self.anaSayfa.winfo_height() / 2,
                                          fill = color, outline = color)
            else:
                rectangle = self.canvas.create_rectangle(
                                        (index - 2) * self.anaSayfa.winfo_width(),
                                        self.anaSayfa.winfo_height(),
                                        self.anaSayfa.winfo_width() / 2,
                                        self.anaSayfa.winfo_height() / 2,
                                        fill = color, outline = color)
            self.dikdortgenler.append(rectangle)
        for id in self.dikdortgenler:
            self.canvas.tag_bind(id, '<ButtonPress-1>', lambda e : self.check_choice())


def main():
    root = tkinter.Tk()
    gui = Simon(root)


if __name__ == "__main__" : main()

