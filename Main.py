import sys
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from CountryMap import CountryMap
from CityNode import CityNode
from PathEdge import PathEdge
from SingletonData import SingletonData
from ViewMap import ViewMap
from tkinter import ttk
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")


LARGE_FONT = ("Verdana", 12)


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)

        # Get data from files
        self.data = SingletonData()

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

        # Get data
        self.data = SingletonData()
        self.Portugal = self.data.Map
        self.Cities = self.data.mapCities

        # Title Label
        label = tk.Label(self, text="Select Cities", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        # OptionMenu Frame
        optionsMenuFrame = tk.Frame(self, width=50, height=40)
        # White canvas Frame
        canvasFrame = tk.Canvas(self, background="white")
        # Method Selector Label
        methodButtonLabel = tk.Label(self, text="Select Search Method")
        # Method Selector Frame
        methodButtonFrame = tk.Frame(self, width=50, height=40)
        # Back button Frame
        backButtonFrame = tk.Frame(self, width=50, height=100)

        # Packing Frames
        backButtonFrame.pack(side="bottom", fill="both", expand=False)
        methodButtonFrame.pack(side="bottom")
        methodButtonLabel.pack(side="bottom")
        optionsMenuFrame.pack(side="top")
        canvasFrame.pack(side="top", fill="both", expand=True)

        ################################################################
        # ListView - prints method iterations
        plotFrame = tk.Frame(canvasFrame)
        listView = tk.Listbox(canvasFrame)
        i = 0
        for city in self.Cities:
            listView.insert(i, city)
            i += 1

        ################################################################

        # Page Items set frames - bottom up
        BackBtn = ttk.Button(backButtonFrame, text="Back to start menu",
                             command=lambda: controller.show_frame(StartPage))

        DfsBtn = ttk.Button(methodButtonFrame, text="DFS")
        UcsBtn = ttk.Button(methodButtonFrame, text="UCS")
        GreedyBtn = ttk.Button(methodButtonFrame, text="Greedy")
        AstarBtn = ttk.Button(methodButtonFrame, text="A*")

        methodSearchLabel = tk.Label(
            methodButtonLabel, text="Select Search Method", font=LARGE_FONT)

        fromCityLabel = tk.Label(optionsMenuFrame, text="FROM")
        fromCityVar = tk.StringVar()  # default value
        fromCityOptionsMenu = ttk.OptionMenu(
            optionsMenuFrame, fromCityVar, self.Cities[0], *self.Cities)

        toCityLabel = tk.Label(optionsMenuFrame, text="TO")
        toCityVar = tk.StringVar()  # default value
        toCityOptionsMenu = ttk.OptionMenu(
            optionsMenuFrame, toCityVar, self.Cities[0], *self.Cities)

        '''
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
        '''

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        # Grid setup
        canvasFrame.grid_columnconfigure(0, weight=1)
        canvasFrame.grid_rowconfigure(0, weight=1)
        plotFrame.grid(row=0, column=0, sticky="nsew")
        listView.grid(row=0, column=1, sticky="nsew")

        canvas = FigureCanvasTkAgg(f, master=plotFrame)
        # canvas.show()
        canvas.get_tk_widget().pack()

        optionsMenuFrame.grid_columnconfigure(0, weight=1)
        fromCityOptionsMenu.grid(row=0, column=1, sticky="w", padx=20)
        toCityOptionsMenu.grid(row=0, column=3, sticky="w")
        fromCityLabel.grid(row=0, column=0, sticky="w")
        toCityLabel.grid(row=0, column=2, sticky="w", padx=20)

        methodButtonLabel.grid_columnconfigure(0, weight=1)
        methodButtonFrame.grid_columnconfigure(0, weight=1)
        DfsBtn.grid(row=0, column=0, sticky="w", pady=20)
        UcsBtn.grid(row=0, column=1, sticky="w", pady=20)
        GreedyBtn.grid(row=0, column=2, sticky="w", pady=20)
        AstarBtn.grid(row=0, column=3, sticky="w", pady=20)

        backButtonFrame.grid_columnconfigure(0, weight=1)
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
