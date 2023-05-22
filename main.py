from autoGame import AutoGame
from tamagotchi import tamagotchi

from tkinter import ttk
from tkinter import messagebox
import customtkinter
from PIL import Image

t: tamagotchi = tamagotchi
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.resizable(False, False)

window_height = 450
window_width = 450

root.geometry(f"{window_height}x{window_width}")

root.title("Tamagotchi")

frame1 = customtkinter.CTkFrame(master=root)
frame1.pack(padx=20, pady=10, fill="both", expand=True)

my_image = customtkinter.CTkImage(Image.open("tamagotchi1.png"), size=(100, 100))
my_image2 = customtkinter.CTkImage(Image.open("tamagotchi2.png"), size=(100, 100))
my_image3 = customtkinter.CTkImage(Image.open("tamagotchi3.png"), size=(100, 100))
my_image4 = customtkinter.CTkImage(Image.open("hamburger.jpg"), size=(100, 100))
my_image5 = customtkinter.CTkImage(Image.open("halfHamburger.jpg"), size=(100, 100))

statok: list[tamagotchi] = []
def Mentés():
    print("Mentés..")
    with open('SaveFile.txt', 'w', encoding='utf-8') as file:
        file.write('nev;karakter;ehseg;elet;kedv;ido\n')
        # file.write(f'karakter = {karakter}\n')
        # file.write(f'Ehseg = {Ehseg}\n')
        # file.write(f'Elet = {Elet}\n')
        # file.write(f'Kedv = {Kedv}\n')
        file.write(f'{Nev};{karakter};{Ehseg};{Elet};{Kedv};')
def Köszöntő():
    global label1
    global label2
    global text
    global button1
    global Nev

    label1 = customtkinter.CTkLabel(master=frame1, text="Szia, üdv a játékunkban!", font=("Roboto", 30))
    label1.pack(padx=10, pady=10)

    label2 = customtkinter.CTkLabel(master=frame1, text="Nevezd el az állatod!", font=("Roboto", 30))
    label2.pack(padx=10, pady=10)

<<<<<<< HEAD
    text = customtkinter.CTkEntry(master=frame1, width=200, justify="center", font=("Roboto", 15))
    text.pack(padx=10, pady=10)
=======
def UpdateSlider(Slider: ttk.Progressbar, value):
    Slider['value'] = value


def Simogatás():
    ClearScreen()
    global EletSlider

    EletSlider = ttk.Progressbar(master=frame1, length=100, variable=Elet)
    EletSlider.pack(padx=10, pady=10)

    UpdateSlider(EletSlider, Elet)

    simogass_meg = customtkinter.CTkLabel(master=frame1, text="Simogass meg!", font=("Roboto", 30))
    simogass_meg.pack(padx=10, pady=10)
    simogat = customtkinter.CTkButton(master=frame1, image=karakter_image, text="", width=120, height=30, command=lambda: ChangeElet(10))
    simogat.pack(padx=10, pady=5)
    vissza_button = customtkinter.CTkButton(master=frame1, text="Lépj ki!", font=("Roboto", 20), command=lambda: Main(karakter))
    vissza_button.pack(padx=10, pady=10)


def Kaja():
    ClearScreen()
    global EhsegSlider

    EhsegSlider = ttk.Progressbar(master=frame1, length=100, variable=Ehseg)
    EhsegSlider.pack(padx=10, pady=10)

    UpdateSlider(EhsegSlider, Ehseg)

    karakter1 = customtkinter.CTkLabel(master=frame1, image=karakter_image, text="", font=("Roboto", 30))
    karakter1.pack(padx=10, pady=10)
    label_etess = customtkinter.CTkLabel(master=frame1, text="Etess meg!", font=("Roboto", 20))
    label_etess.pack(padx=10, pady=10)
    kaja = customtkinter.CTkButton(master=frame1, text="", image=my_image4, font=("Roboto", 30), command=lambda: ChangeEhseg(10))
    kaja.pack(padx=10, pady=10)
    vissza_button = customtkinter.CTkButton(master=frame1, text="Vissza", font=("Roboto", 20), command=lambda: Main(karakter))
    vissza_button.pack(padx=10, pady=10)

>>>>>>> master

    button1 = customtkinter.CTkButton(master=frame1, text="Tovább", width=200, height=30, command=lambda: Választó(text.get()))
    button1.pack(padx=10, pady=5)
    Mentés()
def Main(inp_karakter: str):
    ClearScreen()
    global karakter
    global karakter_image
    global EletSlider
    global EhsegSlider
    global KedvSlider

    karakter = inp_karakter
    if karakter == "kutya":
        label_karakter = customtkinter.CTkLabel(master=frame1, image=my_image, text="", font=("Roboto", 30))
        karakter_image = my_image
        label_karakter.pack(padx=10, pady=10)
    elif karakter == "macska":
        label_karakter = customtkinter.CTkLabel(master=frame1, image=my_image2, text="", font=("Roboto", 30))
        karakter_image = my_image2
        label_karakter.pack(padx=10, pady=10)
    elif karakter == "anyud":
        label_karakter = customtkinter.CTkLabel(master=frame1, image=my_image3, text="", font=("Roboto", 30))
        karakter_image = my_image3
        label_karakter.pack(padx=10, pady=10)

    label_elet = customtkinter.CTkLabel(master=frame1, text="Élet: ", font=("Roboto", 15))
    label_elet.pack(padx=10, pady=3)
    EletSlider = ttk.Progressbar(master=frame1, length=100, variable=Elet)
    EletSlider.pack(padx=10, pady=10)

    UpdateSlider(EletSlider, Elet)

    label_ehseg = customtkinter.CTkLabel(master=frame1, text="Éhség: ", font=("Roboto", 15))
    label_ehseg.pack(padx=10, pady=3)
    EhsegSlider = ttk.Progressbar(master=frame1, length=100, variable=Ehseg)
    EhsegSlider.pack(padx=10, pady=10)

    UpdateSlider(EhsegSlider, Ehseg)

    label_kedv = customtkinter.CTkLabel(master=frame1, text="Kedv: ", font=("Roboto", 15))
    label_kedv.pack(padx=10, pady=3)
    KedvSlider = ttk.Progressbar(master=frame1, length=100, variable=Kedv)
    KedvSlider.pack(padx=10, pady=10)

    UpdateSlider(KedvSlider, Kedv)

<<<<<<< HEAD
    buttonElet = customtkinter.CTkButton(master=frame1, text="Simogatás", width=120, height=30, command=lambda: ChangeElet(10))
=======
    buttonElet = customtkinter.CTkButton(master=frame1, text="Simogatás", width=120, height=30, command=lambda: Simogatás())
>>>>>>> master
    buttonElet.pack(padx=10, pady=5, side="left")
    buttonEhseg = customtkinter.CTkButton(master=frame1, text="Megetetés", width=120, height=30, command=lambda: Kaja())
    buttonEhseg.pack(padx=10, pady=5, side='right')
    buttonKedv = customtkinter.CTkButton(master=frame1, text="Játék állatoddal", width=120, height=30, command=lambda: ChangeKedv(2 * AutoGame.Game()))
    buttonKedv.pack(padx=10, pady=5, side="right")
    Mentés()
try:
    with open('SaveFile.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            statok.append(tamagotchi(sor))
    Nev = t.név
    karakter = t.kar
    Ehseg = int(t.éhség)
    Elet = int(t.élet)
    Kedv = int(t.kedvv)
    Main()

except FileNotFoundError:            
    Nev = ' ' 
    karakter_image = None
    karakter = ""
    Ehseg = 20 
    Elet = 20
    Kedv = 20
    tamagotchi.nev = ''
    tamagotchi.karakter = ''
    tamagotchi.ehseg = 20
    tamagotchi.elet = 20
    tamagotchi.kedv = 20

    Köszöntő()

EletSlider = None
EhsegSlider = None
KedvSlider = None


def UpdateSlider(Slider: ttk.Progressbar, value):
    Slider['value'] = value


def Kaja():
    ClearScreen()
    global EhsegSlider

    EhsegSlider = ttk.Progressbar(master=frame1, length=100, variable=Ehseg)
    EhsegSlider.pack(padx=10, pady=10)

    UpdateSlider(EhsegSlider, Ehseg)

    karakter1 = customtkinter.CTkLabel(master=frame1, image=karakter_image, text="", font=("Roboto", 30))
    karakter1.pack(padx=10, pady=10)
    label_etess = customtkinter.CTkLabel(master=frame1, text="Etess meg!", font=("Roboto", 20))
    label_etess.pack(padx=10, pady=10)
    kaja = customtkinter.CTkButton(master=frame1, text="", image=my_image4, font=("Roboto", 30), command=lambda: ChangeEhseg(10))
    kaja.pack(padx=10, pady=10)
    vissza_button = customtkinter.CTkButton(master=frame1, text="Vissza", font=("Roboto", 20), command=lambda: Main(karakter))
    vissza_button.pack(padx=10, pady=10)




def Választó(text1: str):
    ClearScreen()
    global label3
    global labelanyad
    global bbutton
    global bbutton1
    global bbutton2

    label3 = customtkinter.CTkLabel(master=frame1, text="Az állatod neve: " + text1, font=("Roboto", 30))
    label3.pack(padx=10, pady=10)
    labelanyad = customtkinter.CTkLabel(master=frame1, text="Válaszd ki a karaktered: ", font=("Roboto", 30))
    labelanyad.pack(padx=10, pady=10)

    bbutton = customtkinter.CTkButton(master=frame1, image=my_image, text="", width=30, fg_color="transparent", command=lambda: Main("kutya"))
    bbutton.pack(padx=10, pady=10, side="left")
    bbutton1 = customtkinter.CTkButton(master=frame1, image=my_image2, text="", width=30, fg_color="transparent", command=lambda: Main("macska"))
    bbutton1.pack(padx=10, pady=10, side="right")
    bbutton2 = customtkinter.CTkButton(master=frame1, image=my_image3, text="", width=30, fg_color="transparent", command=lambda: Main("anyud"))
    bbutton2.pack(padx=10, pady=10, side="right")
    Mentés()


<<<<<<< HEAD
=======
def Köszöntő():
    global label1
    global label2
    global text
    global button1

    label1 = customtkinter.CTkLabel(master=frame1, text="Szia, üdv a játékunkban!", font=("Roboto", 30))
    label1.pack(padx=10, pady=10)

    label2 = customtkinter.CTkLabel(master=frame1, text="Nevezd el az állatod!", font=("Roboto", 30))
    label2.pack(padx=10, pady=10)

    text = customtkinter.CTkEntry(master=frame1, width=200, justify="center", font=("Roboto", 15))
    text.pack(padx=10, pady=10)

    button1 = customtkinter.CTkButton(master=frame1, text="Tovább", width=200, height=30, command=lambda: nev_kotelezo(text.get()))
    button1.pack(padx=10, pady=5)
>>>>>>> master


def nev_kotelezo(text):
    if text.strip() == "":
        messagebox.showerror("Hiba", "Kérlek, adj meg egy nevet az állatodnak!")
    else:
        Választó(text)


def ClearScreen():
    for widgets in frame1.winfo_children():
        widgets.destroy()


def ChangeElet(value: int):
    global Elet
    Elet += value
    if Elet > 100:
        Elet = 100
    UpdateSlider(EletSlider, Elet)
    Mentés()


def ChangeKedv(value: int):
    global Kedv
    Kedv += value
    if Kedv > 100:
        Kedv = 100
    UpdateSlider(KedvSlider, Kedv)
    Mentés()


def ChangeEhseg(value: int):
    global Ehseg
    Ehseg += value
    if Ehseg > 100:
        Ehseg = 100
    UpdateSlider(EhsegSlider, Ehseg)
    Mentés()




# def save_kereses():
#     try:
#         with open('SaveFile.txt', 'r', encoding='uft-8')

Mentés()

# Köszöntő()

root.mainloop()

# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false
