import tkinter as tk
from tkinter import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)


        # Grid mit Ressourcen aufbauen
        Label(master, text="Dauer").grid(row=0)
        Label(master, text="Leistung").grid(row=1)
        Label(master, text="Max. Zeit").grid(row=2)

        self.entryDauer = Entry(master)
        self.entryLeistung = Entry(master)
        self.entryMaxZeit = Entry(master)

        self.entryDauer.grid(row=0, column=1)
        self.entryLeistung.grid(row=1, column=1)
        self.entryMaxZeit.grid(row=2, column=1)

        # Initialisierung mit Texten
        self.entryDauer.insert(END, "5")
        self.entryLeistung.insert(END, "10")
        self.entryMaxZeit.insert(END, "20")
        # Events/Methoden mit Buttons verbinden
        self.btnQuit = Button(master, text='Quit', command=root.destroy)\
                       .grid(row=0, column=2, sticky=W, pady=4)
        self.btnStart = Button(master, text='Start', command=self.start)\
                        .grid(row=1, column=2, sticky=W, pady=4)
        self.btnMalen = Button(master, text='Malen', command=self.start)\
                               .grid(row=2, column=2, sticky=W, pady=4)

        # Canvas, also Bitmap
        self.canvas_width = 200
        self.canvas_height = 300
        self.__cvs = Canvas(master, width=self.canvas_width, height=self.canvas_height)
        self.__cvs.grid(row=3, column=1)

    def start(self):
        print("Nn")

root= tk.Tk()
app = Application(master = root)
app.mainloop() 
