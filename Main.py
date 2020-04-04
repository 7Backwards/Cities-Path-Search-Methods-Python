from CountryMap import CountryMap
from CityNode import CityNode
from PathEdge import PathEdge
from SingletonData import SingletonData
from ViewMap import ViewMap
from tkinter import ttk
import tkinter as tk
import sys


LARGE_FONT = ("Verdana", 12)


class Main(tk.Tk):

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
        self.geometry('{}x{}'.format(800, 600))
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, SearchMethodPage, MapPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

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

        self.Portugal = SingletonData().Map

        button1 = ttk.Button(self, text="View Map",
                             command=lambda: ViewMap(self.Portugal).testGraph())
        button1.pack()

        button2 = ttk.Button(self, text="Search Methods",
                             command=lambda: controller.show_frame(SearchMethodPage))
        button2.pack()


class SearchMethodPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Get data from files
        self.data = SingletonData()
        self.Portugal = self.data.Map
        self.Cities = self.data.mapCities

        # Title
        label = tk.Label(self, text="Select Cities", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # OptionMenu
        optionsMenuFrame = tk.Frame(self, width=50, height=40, padx=3, pady=3)
        # White canvas
        canvas = tk.Canvas(self, background="white")

        button_frame = tk.Frame(self, width=50, height=40, padx=3, pady=3)
        buttonBack_frame = tk.Frame(self, width=50, height=100, padx=3, pady=3)

        buttonBack_frame.pack(side="bottom", fill="both", expand=False)
        button_frame.pack(side="bottom")
        optionsMenuFrame.pack(side="top")
        canvas.pack(side="top", fill="both", expand=True)

        ################################################################
        # ListView
        listView = tk.Listbox(canvas)
        i = 0
        for city in self.Cities:
            listView.insert(i, city)
            i += 1

        ################################################################

        DFSBtn = ttk.Button(button_frame, text="DFS")
        UCSBtn = ttk.Button(button_frame, text="UCS")
        GREEDYBtn = ttk.Button(button_frame, text="Greedy")
        ASATRBTN = ttk.Button(button_frame, text="A*")
        BackBtn = ttk.Button(buttonBack_frame, text="Back to start menu",
                             command=lambda: controller.show_frame(StartPage))

        city1Label = tk.Label(optionsMenuFrame, text="City 1")
        variable1 = tk.StringVar()  # default value
        optionsMenu1 = ttk.OptionMenu(
            optionsMenuFrame, variable1, self.Cities[0], *self.Cities)

        city2Label = tk.Label(optionsMenuFrame, text="City 2")
        variable2 = tk.StringVar()  # default value
        optionsMenu2 = ttk.OptionMenu(
            optionsMenuFrame, variable2, self.Cities[0], *self.Cities)

        #####################TEST BUTTONS#################################
        def ok1():
            print("value is:" + variable1.get())

        def ok2():
            print("value is:" + variable2.get())

        button1 = ttk.Button(self, text="Test City 1", command=ok1)
        button1.pack()
        button2 = ttk.Button(self, text="Test City 2", command=ok2)
        button2.pack()
        ##################################################################

        canvas.grid_columnconfigure(0, weight=1)
        canvas.grid_rowconfigure(0, weight=1)
        optionsMenuFrame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)
        buttonBack_frame.grid_columnconfigure(0, weight=1)

        listView.grid(row=0, column=1, sticky="nsew")
        optionsMenu1.grid(row=0, column=1, sticky="w", padx=20)
        optionsMenu2.grid(row=0, column=3, sticky="w")
        city1Label.grid(row=0, column=0, sticky="w")
        city2Label.grid(row=0, column=2, sticky="w", padx=20)
        DFSBtn.grid(row=0, column=0, sticky="w", pady=20)
        UCSBtn.grid(row=0, column=1, sticky="w", pady=20)
        GREEDYBtn.grid(row=0, column=2, sticky="w", pady=20)
        ASATRBTN.grid(row=0, column=3, sticky="w", pady=20)
        BackBtn.grid(row=0, column=0, sticky="e", pady=20)


class MapPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Map Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to start menu",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        # Get data from files
        self.data = SingletonData()
        self.Portugal = self.data.Map

        button2 = ttk.Button(self, text="test graph",
                             command=lambda: ViewMap(self.Portugal).testGraph())
        button2.pack()


app = Main()
app.mainloop()
