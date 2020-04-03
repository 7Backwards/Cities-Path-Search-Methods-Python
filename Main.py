from CountryMap import CountryMap
from CityNode import CityNode
from PathEdge import PathEdge
from SingletonData import SingletonData
from ViewMap import ViewMap
from tkinter import ttk
import csv
import tkinter as tk
import sys
import matplotlib.pyplot as plt
plt.ion()


LARGE_FONT = ("Verdana", 12)


class Main(tk.Tk):

    data = None
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)

        # Get data from files
        self.data = SingletonData()
        self.Portugal = self.data.Map
        self.Cities = self.data.mapCities
        
        
        
        if sys.platform.startswith('win'):
            tk.Tk.iconbitmap(self, default='Res/favicon.ico')

        tk.Tk.wm_title(self, "IA - Search Methods")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, SearchMethodPage, MapPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        ################################################################
        # List Test
        self.list = tk.Listbox(self)
        i = 0
        for city in self.Cities:
            self.list.insert(i, city)
            i += 1
        self.list.pack()

        # OptionMenuTest
        variable = tk.StringVar()  # default value
        w = ttk.OptionMenu(self, variable, self.Cities[0], *self.Cities)
        w.pack()

        def ok():
            print("value is:" + variable.get())

        button = ttk.Button(self, text="OK", command=ok)
        button.pack()
        ################################################################

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, text="Map Search Methods - 2020", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Get data from files
        self.data = SingletonData()
        self.Portugal = self.data.Map
        
        button1 = ttk.Button(self, text="View Map",
                             command=lambda: ViewMap(self.Portugal).testGraph())
        button1.pack()

        button2 = ttk.Button(self, text="Search Methods",
                             command=lambda: controller.show_frame(SearchMethodPage))
        button2.pack()


class SearchMethodPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select Cities", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to start menu",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


class MapPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Map Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to start menu",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


        
        button2 = ttk.Button(self, text="test graph",
                             command=lambda: ViewMap().testGraph())
        button2.pack()


app = Main()
app.mainloop()
ViewMap(Main.data.Map).addLine("Leiria","Lisboa")
