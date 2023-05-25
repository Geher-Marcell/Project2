from autoGame import AutoGame
from tamagotchi import tamagotchi
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox
import customtkinter
from PIL import Image

timeformat = '%m/%d/%y %H:%M:%S'

tamagotchi1 = customtkinter.CTkImage(Image.open("images/tamagotchi1.png"), size=(100, 100))
tamagotchi2 = customtkinter.CTkImage(Image.open("images/tamagotchi2.png"), size=(100, 100))
tamagotchi3 = customtkinter.CTkImage(Image.open("images/tamagotchi3.png"), size=(100, 100))
hamburger_full = customtkinter.CTkImage(Image.open("images/hamburger.jpg"), size=(100, 100))
hamburger_half = customtkinter.CTkImage(Image.open("images/halfHamburger.jpg"), size=(100, 100))

t: tamagotchi = tamagotchi()
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.resizable(False, False)

window_height = 450
window_width = 450

root.geometry(f"{window_height}x{window_width}")

root.title("Tamagotchi")

frame1 = customtkinter.CTkFrame(master=root)
frame1.pack(padx=20, pady=10, fill="both", expand=True)

# statok: list[tamagotchi] = []


EletSlider = None
EhsegSlider = None
KedvSlider = None


def ClearScreen():
    for widgets in frame1.winfo_children():
        widgets.destroy()


def Mentés():
    print("Mentés..")
    with open('SaveFile.txt', 'w', encoding='utf-8') as file:
        file.write('nev;karakter;ehseg;elet;kedv;ido\n')

        currentDate = str(datetime.now().strftime(timeformat))
        file.write(f'{t.Nev};{t.Karakter};{t.Ehseg};{t.Elet};{t.Kedv};{currentDate}')


def Köszöntő():
    label1 = customtkinter.CTkLabel(master=frame1, text="Szia, üdv a játékunkban!", font=("Roboto", 30))
    label1.pack(padx=10, pady=10)

    label2 = customtkinter.CTkLabel(master=frame1, text="Nevezd el az állatod!", font=("Roboto", 30))
    label2.pack(padx=10, pady=10)

    text = customtkinter.CTkEntry(master=frame1, width=200, justify="center", font=("Roboto", 15))
    text.pack(padx=10, pady=10)

    button1 = customtkinter.CTkButton(master=frame1, text="Tovább", width=200, height=30, command=lambda: Választó(text.get()))
    button1.pack(padx=10, pady=5)
    Mentés()


def UpdateSlider(Slider: ttk.Progressbar, value):
    Slider['value'] = value


def Simogatás():
    ClearScreen()

    EletSlider = ttk.Progressbar(master=frame1, length=100, variable=t.Elet)
    EletSlider.pack(padx=10, pady=10)

    UpdateSlider(EletSlider, t.Elet)

    simogass_meg = customtkinter.CTkLabel(master=frame1, text="Simogass meg!", font=("Roboto", 30))
    simogass_meg.pack(padx=10, pady=10)
    simogat = customtkinter.CTkButton(master=frame1, image=t.image, text="", width=120, height=30, command=lambda: ChangeElet(10))
    simogat.pack(padx=10, pady=5)
    vissza_button = customtkinter.CTkButton(master=frame1, text="Lépj ki!", font=("Roboto", 20), command=lambda: Main(t.Karakter))
    vissza_button.pack(padx=10, pady=10)


def Kaja():
    ClearScreen()

    EhsegSlider = ttk.Progressbar(master=frame1, length=100, variable=t.Ehseg)
    EhsegSlider.pack(padx=10, pady=10)

    UpdateSlider(EhsegSlider, t.Ehseg)

    karakter1 = customtkinter.CTkLabel(master=frame1, image=t.image, text="", font=("Roboto", 30))
    karakter1.pack(padx=10, pady=10)
    label_etess = customtkinter.CTkLabel(master=frame1, text="Etess meg!", font=("Roboto", 20))
    label_etess.pack(padx=10, pady=10)
    kaja = customtkinter.CTkButton(master=frame1, text="", image=hamburger_full, font=("Roboto", 30), command=lambda: ChangeEhseg(10))
    kaja.pack(padx=10, pady=10)
    vissza_button = customtkinter.CTkButton(master=frame1, text="Vissza", font=("Roboto", 20), command=lambda: Main(t.Karakter))
    vissza_button.pack(padx=10, pady=10)

    # , command=lambda: Választó(text.get())

    button1 = customtkinter.CTkButton(master=frame1, text="Tovább", width=200, height=30)
    button1.pack(padx=10, pady=5)
    Mentés()


def Main(inp_karakter: str):
    ClearScreen()

    karakter = inp_karakter
    if karakter == "kutya":
        label_karakter = customtkinter.CTkLabel(master=frame1, image=tamagotchi1, text="", font=("Roboto", 30))
        t.image = tamagotchi1
        label_karakter.pack(padx=10, pady=10)
    elif karakter == "macska":
        label_karakter = customtkinter.CTkLabel(master=frame1, image=tamagotchi2, text="", font=("Roboto", 30))
        t.image = tamagotchi2
        label_karakter.pack(padx=10, pady=10)
    elif karakter == "anyud":
        label_karakter = customtkinter.CTkLabel(master=frame1, image=tamagotchi3, text="", font=("Roboto", 30))
        t.image = tamagotchi3
        label_karakter.pack(padx=10, pady=10)

    label_elet = customtkinter.CTkLabel(master=frame1, text="Élet: ", font=("Roboto", 15))
    label_elet.pack(padx=10, pady=3)
    EletSlider = ttk.Progressbar(master=frame1, length=100, variable=t.Elet)
    EletSlider.pack(padx=10, pady=10)

    UpdateSlider(EletSlider, t.Elet)

    label_ehseg = customtkinter.CTkLabel(master=frame1, text="Éhség: ", font=("Roboto", 15))
    label_ehseg.pack(padx=10, pady=3)
    EhsegSlider = ttk.Progressbar(master=frame1, length=100, variable=t.Ehseg)
    EhsegSlider.pack(padx=10, pady=10)

    UpdateSlider(EhsegSlider, t.Ehseg)

    label_kedv = customtkinter.CTkLabel(master=frame1, text="Kedv: ", font=("Roboto", 15))
    label_kedv.pack(padx=10, pady=3)
    KedvSlider = ttk.Progressbar(master=frame1, length=100, variable=t.Kedv)
    KedvSlider.pack(padx=10, pady=10)

    UpdateSlider(KedvSlider, t.Kedv)

    buttonElet = customtkinter.CTkButton(master=frame1, text="Simogatás", width=120, height=30, command=lambda: Simogatás())
    buttonElet.pack(padx=10, pady=5, side="left")
    buttonEhseg = customtkinter.CTkButton(master=frame1, text="Megetetés", width=120, height=30, command=lambda: Kaja())
    buttonEhseg.pack(padx=10, pady=5, side='right')
    buttonKedv = customtkinter.CTkButton(master=frame1, text="Játék állatoddal", width=120, height=30, command=lambda: ChangeKedv(2 * AutoGame.Game()))
    buttonKedv.pack(padx=10, pady=5, side="right")
    Mentés()


def Beolvasas():
    try:
        with open('SaveFile.txt', 'r', encoding='utf-8') as file:
            for sor in file.read().splitlines()[1:]:
                # statok.append(tamagotchi(sor))
                adatok = sor.split(';')
                n = adatok[0]
                k = adatok[1]
                Eh = int(adatok[2])
                El = int(adatok[3])
                Ke = int(adatok[4])

                t.loadSave(n, k, Eh, El, Ke)

                print("ido: ", adatok[5])

        Main(t.Karakter)

    except FileNotFoundError:
        Köszöntő()


def Választó(text1: str):
    ClearScreen()

    label3 = customtkinter.CTkLabel(master=frame1, text="Az állatod neve: " + text1, font=("Roboto", 30))
    label3.pack(padx=10, pady=10)
    labelanyad = customtkinter.CTkLabel(master=frame1, text="Válaszd ki a karaktered: ", font=("Roboto", 30))
    labelanyad.pack(padx=10, pady=10)

    bbutton = customtkinter.CTkButton(master=frame1, image=tamagotchi1, text="", width=30, fg_color="transparent", command=lambda: Main("kutya"))
    bbutton.pack(padx=10, pady=10, side="left")
    bbutton1 = customtkinter.CTkButton(master=frame1, image=tamagotchi2, text="", width=30, fg_color="transparent", command=lambda: Main("macska"))
    bbutton1.pack(padx=10, pady=10, side="right")
    bbutton2 = customtkinter.CTkButton(master=frame1, image=tamagotchi3, text="", width=30, fg_color="transparent", command=lambda: Main("anyud"))
    bbutton2.pack(padx=10, pady=10, side="right")
    Mentés()


def nev_kotelezo(text):
    if text.strip() == "":
        messagebox.showerror("Hiba", "Kérlek, adj meg egy nevet az állatodnak!")
    else:
        Választó(text)


def ChangeElet(value: int):

    t.Elet += value
    if t.Elet > 100:
        t.Elet = 100
    UpdateSlider(EletSlider,t. Elet)
    Mentés()


def ChangeKedv(value: int):

    t.Kedv += value
    if t.Kedv > 100:
        t.Kedv = 100
    UpdateSlider(KedvSlider, t.Kedv)
    Mentés()


def ChangeEhseg(value: int):

    t.Ehseg += value
    if t.Ehseg > 100:
        t.Ehseg = 100
    UpdateSlider(EhsegSlider, t.Ehseg)
    Mentés()


Beolvasas()

Mentés()

# Köszöntő()

root.mainloop()

# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false
