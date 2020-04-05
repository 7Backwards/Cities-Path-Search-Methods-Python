import sys
from matplotlib.figure import Figure
from matplotlib import style
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
style.use("ggplot")


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)

        # Get data from files
        self.data = SingletonData()

        if sys.platform.startswith('win'):
            tk.Tk.iconbitmap(self, default='Res/favicon.ico')

        tk.Tk.wm_title(self, "IA - Search Methods")

        container = tk.Frame(self)
        self.geometry('{}x{}'.format(1024, 768))
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
                             command=lambda: ViewMap(self.Portugal, []).testGraph())
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

        # Setup GUI
        # Title Label
        self.labelFrame = tk.Label(self, text="Select Cities", font=LARGE_FONT)
        # OptionMenu Frame
        self.optionsMenuFrame = tk.Frame(self)
        # White canvas Frame
        self.canvasFrame = tk.Canvas(self, background="white")
        # Method Selector Label
        self.methodButtonLabel = tk.Label(self, text="Select Search Method")
        # Method Selector Frame
        self.methodButtonFrame = tk.Frame(self, width=50, height=20)
        # Back button Frame
        self.backButtonFrame = tk.Frame(self, width=50, height=40)
        # ListView - prints method iterations
        self.plotFrame = tk.Frame(self.canvasFrame)
        self.IterationList = tk.Listbox(self.canvasFrame, width=80)

        # Packing Frames
        self.backButtonFrame.pack(side="bottom", fill="both", expand=False)
        self.methodButtonFrame.pack(side="bottom")
        self.methodButtonLabel.pack(side="bottom")
        self.labelFrame.pack(side="top")
        self.optionsMenuFrame.pack(side="top")
        self.canvasFrame.pack(side="top", fill="both", expand=True)

        # Page Items set frames - bottom up
        BackBtn = ttk.Button(self.backButtonFrame, text="Back to start menu",
                             command=lambda: controller.show_frame(StartPage))

        DfsBtn = ttk.Button(self.methodButtonFrame, text="DFS")
        UcsBtn = ttk.Button(self.methodButtonFrame, text="UCS")
        GreedyBtn = ttk.Button(self.methodButtonFrame, text="Greedy")
        AstarBtn = ttk.Button(self.methodButtonFrame,
                              text="A*", command=self.refreshCanvas)

        self.methodSearchLabel = tk.Label(
            self.methodButtonLabel, text="Select Search Method", font=LARGE_FONT)

        self.fromCityLabel = tk.Label(self.optionsMenuFrame, text="FROM")
        fromCityVar = tk.StringVar()  # default value
        fromCityOptionsMenu = ttk.OptionMenu(
            self.optionsMenuFrame, fromCityVar, self.Cities[0], *self.Cities)

        toCityLabel = tk.Label(self.optionsMenuFrame, text="TO")
        toCityVar = tk.StringVar()  # default value
        toCityOptionsMenu = ttk.OptionMenu(
            self.optionsMenuFrame, toCityVar, self.Cities[0], *self.Cities)

        # Grid setup
        self.canvasFrame.grid_columnconfigure(0, weight=1)
        self.canvasFrame.grid_rowconfigure(0, weight=1)
        self.plotFrame.grid(row=0, column=0, sticky="nsew")
        self.IterationList.grid(row=0, column=1, sticky="nsew")

        # Test paths
        arrayPath = []
        # arrayPath.append(self.Portugal.pathsMap[1])

        self.canvas = FigureCanvasTkAgg(
            ViewMap(self.Portugal, arrayPath).testGraph(), master=self.plotFrame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        self.optionsMenuFrame.grid_columnconfigure(0, weight=1)
        fromCityOptionsMenu.grid(row=0, column=1, sticky="w", padx=20)
        toCityOptionsMenu.grid(row=0, column=3, sticky="w")
        self.fromCityLabel.grid(row=0, column=0, sticky="w")
        self.fromCityLabel.grid(row=0, column=0, sticky="w")
        toCityLabel.grid(row=0, column=2, sticky="w", padx=20)

        self.methodButtonLabel.grid_columnconfigure(0, weight=1)
        self.methodButtonFrame.grid_columnconfigure(0, weight=1)
        DfsBtn.grid(row=0, column=0, sticky="w", pady=20)
        UcsBtn.grid(row=0, column=1, sticky="w", pady=20)
        GreedyBtn.grid(row=0, column=2, sticky="w", pady=20)
        AstarBtn.grid(row=0, column=3, sticky="w", pady=20)

        self.backButtonFrame.grid_columnconfigure(0, weight=1)
        BackBtn.grid(row=0, column=0, sticky="e", pady=20)

    def refreshCanvas(self):
        try:
            self.canvas.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        # Test paths
        arrayPath = []
        arrayPath.append(self.Portugal.pathsMap[1])

        self.canvas = FigureCanvasTkAgg(
            ViewMap(self.Portugal, arrayPath).testGraph(), master=self.plotFrame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        matplotlib.pyplot.close('all')


class MapPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Map Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to start menu",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="test graph",
                             command=lambda: ViewMap(SingletonData().Map, []).testGraph())
        button2.pack()


app = Main()
matplotlib.pyplot.close('all')
app.lift()
app.attributes('-topmost', True)
app.after_idle(app.attributes, '-topmost', False)
app.mainloop()
