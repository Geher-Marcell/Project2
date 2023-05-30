from autoGame import AutoGame
from tamagotchi import tamagotchi
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox
import customtkinter
from PIL import Image
import os

timeformat = '%m/%d/%y %H:%M:%S'
kepeleres = "images/tamagotchies/"

hamburger_full = customtkinter.CTkImage(Image.open("images/hamburger.jpg"), size=(100, 100))

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


def ClearScreen():
    for widgets in frame1.winfo_children():
        widgets.destroy()

def mentés_törlése():
    os.system('cmd /k "del SaveFile.txt')

def Mentés():
    with open('SaveFile.txt', 'w', encoding='utf-8') as file:
        file.write('nev;karakter;ehseg;elet;kedv;ido\n')

        currentDate = str(datetime.now().strftime(timeformat))
        file.write(f'{t.Nev};{t.Karakter};{t.Ehseg};{t.Elet};{t.Kedv};{currentDate}')


def Név_Választó():
    label1 = customtkinter.CTkLabel(master=frame1, text="Szia, üdv a játékunkban!", font=("Roboto", 30))
    label1.pack(padx=10, pady=10)

    label2 = customtkinter.CTkLabel(master=frame1, text="Nevezd el az állatod!", font=("Roboto", 30))
    label2.pack(padx=10, pady=10)

    text = customtkinter.CTkEntry(master=frame1, width=200, justify="center", font=("Roboto", 15))
    text.pack(padx=10, pady=10)

    button1 = customtkinter.CTkButton(master=frame1, text="Tovább", width=200, height=30, command=lambda: Karakter_Választó(text.get()))
    button1.pack(padx=10, pady=5)
    Mentés()


def UpdateSlider(Slider: ttk.Progressbar, value):
    Slider['value'] = value


def Simogatás():
    global EletSlider

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
    global EhsegSlider

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

    Mentés()


def Main(*args):
    global EletSlider
    global EhsegSlider
    global KedvSlider

    ClearScreen()

    if len(args) > 0:
        t.Karakter = args[0]


    label_nev = customtkinter.CTkLabel(master=frame1, text=f"{t.Nev}", font=("Roboto", 30, "bold"))
    label_nev.pack(padx=10)

    # Az állatka megjelítése
    image = kepmegnyitas(t.Karakter, kepeleres)
    label_karakter = customtkinter.CTkLabel(master=frame1, image=image, text="", font=("Roboto", 30))
    label_karakter.pack(padx=10,pady=10)

    t.image = image

    # Élet slider
    label_elet = customtkinter.CTkLabel(master=frame1, text="Élet: ", font=("Roboto", 15))
    label_elet.pack(padx=10, pady=3)
    EletSlider = ttk.Progressbar(master=frame1, length=100, variable=t.Elet)
    EletSlider.pack(padx=10, pady=10)

    UpdateSlider(EletSlider, t.Elet)

    # Éhség slider
    label_ehseg = customtkinter.CTkLabel(master=frame1, text="Éhség: ", font=("Roboto", 15))
    label_ehseg.pack(padx=10, pady=3)
    EhsegSlider = ttk.Progressbar(master=frame1, length=100, variable=t.Ehseg)
    EhsegSlider.pack(padx=10, pady=10)

    UpdateSlider(EhsegSlider, t.Ehseg)

    # Kedv slider
    label_kedv = customtkinter.CTkLabel(master=frame1, text="Kedv: ", font=("Roboto", 15))
    label_kedv.pack(padx=10, pady=3)
    KedvSlider = ttk.Progressbar(master=frame1, length=100, variable=t.Kedv)
    KedvSlider.pack(padx=10, pady=10)

    UpdateSlider(KedvSlider, t.Kedv)

    # Gombok
    buttonElet = customtkinter.CTkButton(master=frame1, text="Simogatás", width=120, height=30, command=lambda: Simogatás())
    buttonElet.pack(padx=10, pady=5, side="left")
    buttonEhseg = customtkinter.CTkButton(master=frame1, text="Megetetés", width=120, height=30, command=lambda: Kaja())
    buttonEhseg.pack(padx=10, pady=5, side='right')
    buttonKedv = customtkinter.CTkButton(master=frame1, text="Játék állatoddal", width=120, height=30, command=lambda: jatekValaszto())
    buttonKedv.pack(padx=10, pady=5, side="right")
    Mentés()

def jatekValaszto():
    global KedvSlider
    ClearScreen()

    KedvSlider = ttk.Progressbar(master=frame1, length=100, variable=t.Kedv)
    KedvSlider.pack(padx=10, pady=10)

    UpdateSlider(KedvSlider, t.Kedv)

    auto_btn = customtkinter.CTkButton(master=frame1, text="Autóverseny", font=("Roboto", 20), command=lambda: ChangeKedv(2 * AutoGame.Game()))
    auto_btn.pack(padx=10, pady=10)

    vissza_button = customtkinter.CTkButton(master=frame1, text="Vissza", font=("Roboto", 20), command=lambda: Main(t.Karakter))
    vissza_button.pack(padx=10, pady=10)


def Beolvasas():
    try:
        with open('SaveFile.txt', 'r', encoding='utf-8') as file:
            for sor in file.read().splitlines()[1:]:
                
                adatok = sor.split(';')
                n = adatok[0]
                k = adatok[1]
                Eh = int(adatok[2])
                El = int(adatok[3])
                Ke = int(adatok[4])

                t.loadSave(n, k, Eh, El, Ke)

                eltelt_ido = (datetime.now() - datetime.strptime(adatok[5], timeformat)).total_seconds()
                t.Ehseg = clamp(int(t.Ehseg - (eltelt_ido / 10)), 0, 100)
                t.Elet = clamp(int(t.Elet - (eltelt_ido / 10)), 0, 100)
                t.Kedv = clamp(int(t.Kedv - (eltelt_ido / 10)), 0, 100)
        if not meghalt_e():
            Main(t.Karakter)
        else:
            messagebox.showerror('R.I.P', f'Sajnáljuk, de {t.Nev} elpusztult :(')
            mentés_törlése()
            exit()

    except FileNotFoundError:
        Név_Választó()


def Karakter_Választó(név: str):
    ClearScreen()

    t.Nev = név
    label3 = customtkinter.CTkLabel(master=frame1, text="Az állatod neve: " + név, font=("Roboto", 30))
    label3.pack(padx=10, pady=10)
    #label3.grid(row=0, column=0, padx=10, pady=10)

    labelanyad = customtkinter.CTkLabel(master=frame1, text="Válaszd ki a karaktered: ", font=("Roboto", 30))
    labelanyad.pack(padx=10, pady=10)
    #labelanyad.grid(row=1, column=0, padx=10, pady=10)

    image_names = [os.path.splitext(f)[0] for f in os.listdir(kepeleres) if os.path.isfile(os.path.join(kepeleres, f)) and f.endswith('.png')]

    # TODO: SPACING A KÉPEK KÖZÖTT
    for i in range(len(image_names)):
        bbutton = customtkinter.CTkButton(master=frame1, image=kepmegnyitas(image_names[i], kepeleres, (300/len(image_names))), text="", width=30, fg_color="transparent", command=lambda i=i: Main(image_names[i]))
        ##bbutton.grid(row=5, column=i, sticky="W")
        bbutton.pack(padx=10, pady=10, side="left", )

    Mentés()


def kepmegnyitas(kepnev, kepeleres, size=100):
        return customtkinter.CTkImage(Image.open(kepeleres + kepnev + ".png"), size=(size, size))


def nev_kotelezo(név):
    if név.strip() == "":
        messagebox.showerror("Hiba", "Kérlek, adj meg egy nevet az állatodnak!")
    else:
        Karakter_Választó(név)

def meghalt_e():
    if t.Ehseg == 0 or t.Elet == 0 or t.Kedv == 0:
        return True
    return False


def ChangeElet(value: int):
    t.Elet = clamp(t.Elet + value, 0, 100)

    UpdateSlider(EletSlider, t.Elet)
    Mentés()


def ChangeKedv(value: int):
    t.Kedv = clamp(t.Kedv + value, 0, 100)

    UpdateSlider(KedvSlider, t.Kedv)
    Mentés()


def ChangeEhseg(value: int):
    t.Ehseg = clamp(t.Ehseg + value, 0, 100)

    UpdateSlider(EhsegSlider, t.Ehseg)
    Mentés()

    
def clamp(number, min_value, max_value):
    return max(min(number, max_value), min_value)

Beolvasas()

root.mainloop()

# pyright: reportMissingTypeStubs=false
# pyright: reportUnknownMemberType=false
