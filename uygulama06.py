import random
from tkinter import Tk, Label, Button

class SaglıklıYasamBilgileri:
    def __init__(self, anaSayfa):
        self.anaSayfa= anaSayfa
        anaSayfa.title=("Sağlıklı Yaşam Bilgisi")

        self.label= Label(anaSayfa, text="Sağlıklı Yaşam Bilgileri",font=("Arial",12),bg="light blue")
        self.label.pack()

        self.saglık= Button(anaSayfa, text="Merhabalar",font=("arial",11), command= self.bilgi,bg="pink")
        self.saglık.pack()

        self.saglık_butonu= Button(anaSayfa, text="Bilgiyi Görmek İçin Tıkla",font=("arial",11),command=self.gunun_bilgisi,bg="pink")
        self.saglık_butonu.pack()

        self.kapat=Button(anaSayfa, text="Kapat",font=("arial",11),command= anaSayfa.quit,bg="brown")
        self.kapat.pack()

    def bilgi(self):
        print("Merhabalar!!!")

    def gunun_bilgisi(self):
        bilgiler=("Günde iki litre su tüketiniz.","Sebze ve meyveyi bol tüketiniz.", "Kahvaltı yapmayı ihmal etmeyiniz.", "Fazla güneşten korununuz.","Stresi azaltınız.","Düzenli uyumalısınız.","Haftada en az üç gün açık havada yürüyünüz.","Gereksiz ilaç kullanmayınız.","Düzenli egzersiz yapınız","Pozitif olunuz.")
        secilenBilgi=random.choice(bilgiler)
        self.bilgiler= Label(self.anaSayfa, text=secilenBilgi)
        self.bilgiler.pack()

root=Tk()
my_gui=SaglıklıYasamBilgileri(root)
root.mainloop()