import tkinter as tk
import customtkinter as ctk
import pandas as pd
import pykakasi
import random

from pandas import *
from PIL import ImageTk, Image

class Read_Write_Seen:
    #En un archivo verificamos aquellas palabras marcadas como vistas
    def Read_Seen():
        Aprendida = open("C:/Users/Eingel/Documents/Angel/Aprende_Kotobas/Dataset/KotobaVista.dat", "r")
        Lineas = []
        for x in range(7831):
            valor = Aprendida.readline()
            valor = int(valor)
            if (valor == 1):
                Lineas.append(x)
        Aprendida.close()
        return Lineas
    #Aqui podemos reiniciar el archivo que guarda las palabras vistas
    def Reset_Seen():
        Archivo = open("C:/Users/Eingel/Documents/Angel/Aprende_Kotobas/Dataset/KotobaVista.dat", "w")
        for z in range(7831):
            Archivo.write("0" + "\n")
        Archivo.close()

reset = bool(False)
if (reset == True):
    Read_Write_Seen.Reset_Seen()

vistos = Read_Write_Seen.Read_Seen()
print(vistos)

i = random.randint(0,2136) #Para Kanjis
j = random.randint(0,7831) #Para palabras
KanjiVisto = []
KotobaVista = []

for x in range(2136):
    KanjiVisto.append(0)

for y in range(7831):
    KotobaVista.append(0)

KanjiVisto[i] = 1
KotobaVista[j] = 1

vista = open("C:/Users/Eingel/Documents/Angel/Aprende_Kotobas/Dataset/KotobaVista.dat", "w")

for z in range(7831):
    for a in range(len(vistos)):
        if (vistos[a] == z):
            KotobaVista[z] = 1
    vista.write(str(KotobaVista[z]) + "\n")
vista.close()

print(i,j)

app = tk.Tk()
app.geometry("532x622")
app.title("Japanese Teacher")
ctk.set_appearance_mode("dark")

prompt = ctk.CTkEntry(master=app, height=40, width=512, fg_color="white", text_color="black")
prompt.place(x=10, y=450)

lmain = ctk.CTkLabel(master=app, height=512, width=512)
lmain.place(x=10,y=500)

image1 = Image.open("C:/Users/Eingel/Documents/Angel/Aprende_Kotobas/Images/ことば.jpg")
image1 = image1.resize((450,450), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(image=test)
label1.image = test
label1.place(x=40, y=10)

trigger = ctk.CTkButton(master=app, height=40, width=120, fg_color="white", text_color="blue")
trigger.configure(text="Nueva Kotoba")
trigger.place(x=206, y=500)

JapVob = read_csv("C:/Users/Eingel/Documents/Angel/Aprende_Kotobas/Dataset/Japanese_Vocabolary_Dataset.csv")
HiraganaKotoba = JapVob['Hiragana'].tolist()
RomajiKotoba = JapVob['Romaji'].tolist()
KanjiKotoba = JapVob['Kanji'].tolist()
EnglishKotoba = JapVob['English_Meaning'].tolist()
ExampleKotoba = JapVob['Example'].tolist()

KanjiVob = read_csv("C:/Users/Eingel/Documents/Angel/Aprende_Kotobas/Dataset/Kanji_Levels.csv")
KanjiKanji = KanjiVob['kanji'].tolist()
OnKanji = KanjiVob['on'].tolist()
OnRomajiKanji = KanjiVob['romaji on'].tolist()
KunKanji = KanjiVob['kun'].tolist()
KunRomajiKanji = KanjiVob['romaji kun'].tolist()
EnglishKanji = KanjiVob['meaning'].tolist()
LevelKanji = KanjiVob['level'].tolist()
OnKunKanji = KanjiVob['on…romaji kun'].tolist()

print(HiraganaKotoba[j], RomajiKotoba[j], KanjiKotoba[j], EnglishKotoba[j], ExampleKotoba[j])
print(KanjiKanji[i], OnKanji[i], OnRomajiKanji[i], KunKanji[i],KunRomajiKanji[i],EnglishKanji[i],LevelKanji[i],OnKunKanji[i])

app.mainloop()