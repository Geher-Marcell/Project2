from tkinter import ttk
import customtkinter
from PIL import Image
import pygame
import pygame.locals
import random

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


def tab1():
    def tab2(text1: str):
        label1.destroy()
        label2.destroy()
        text.destroy()
        button1.destroy()

        label3 = customtkinter.CTkLabel(master=frame1, text="Az állatod neve: " + text1, font=("Roboto", 30))
        label3.pack(padx=10, pady=10)
        labelanyad = customtkinter.CTkLabel(master=frame1, text="Válaszd ki a karaktered: ", font=("Roboto", 30))
        labelanyad.pack(padx=10, pady=10)

        bbutton = customtkinter.CTkButton(master=frame1, image=my_image, text="", width=30, fg_color="transparent", command=lambda: tab3("kutya"))
        bbutton.pack(padx=10, pady=10, side="left")
        bbutton1 = customtkinter.CTkButton(master=frame1, image=my_image2, text="", width=30, fg_color="transparent", command=lambda: tab3("macska"))
        bbutton1.pack(padx=10, pady=10, side="right")
        bbutton2 = customtkinter.CTkButton(master=frame1, image=my_image3, text="", width=30, fg_color="transparent", command=lambda: tab3("anyud"))
        bbutton2.pack(padx=10, pady=10, side="right")

    label1 = customtkinter.CTkLabel(master=frame1, text="Szia, üdv a játékunkban!", font=("Roboto", 30))
    label1.pack(padx=10, pady=10)

    label2 = customtkinter.CTkLabel(master=frame1, text="Nevezd el az állatod!", font=("Roboto", 30))
    label2.pack(padx=10, pady=10)

    text = customtkinter.CTkEntry(master=frame1, width=200, justify="center", font=("Roboto", 15))
    text.pack(padx=10, pady=10)

    button1 = customtkinter.CTkButton(master=frame1, text="Tovább", width=200, height=30, command=lambda: tab2(text.get()))
    button1.pack(padx=10, pady=5)


tab1()
root.mainloop()
