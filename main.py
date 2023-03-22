from tkinter import *

window_height = 300
window_width = 300

root = Tk()
root.title("xd")
root.geometry(f"{window_height}x{window_width}")

feedButton = Button(root, text="Feed")
feedButton.place(x=25, y=window_height - 50)

playButton = Button(root, text="Play")
playButton.place(x=window_width / 2 - 15, y=window_height - 50)

exitButton = Button(root, text="Exit")
exitButton.place(x=window_width - 50, y=window_height - 50)


root.mainloop()
