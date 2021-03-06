import sys
from os import system, name
from subprocess import call
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
from SingletonData import SingletonData
from ViewMap import ViewMap
from SearchGraphIDDFS import SearchGraphIDDFS as IDDFS
from SearchGraphUCS import SearchGraphUCS as UCS
from SearchGraphGREEDY import SearchGraphGREEDY as GREEDY
from SearchGraphASTAR import SearchGraphASTAR as ASTAR


matplotlib.use("TkAgg")

DEBUG = True
LARGE_FONT = ("Verdana", 12)
style.use("ggplot")


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)

        # Get data from files
        self.data = SingletonData()

        self.attributes("-fullscreen", True)
        self.bind("<Escape>", self.end_fullscreen)

        if sys.platform.startswith('win'):
            tk.Tk.iconbitmap(self, default='Res/favicon.ico')

        tk.Tk.wm_title(self, "IA - Search Methods")

        container = tk.Frame(self)
        # self.geometry('{}x{}'.format(1024, 768))
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, SearchMethodPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def end_fullscreen(self, event=None):
        self.attributes("-fullscreen", False)
        return "break"


class SearchMethodPage(tk.Frame):

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


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Get data
        self.data = SingletonData()
        self.Portugal = self.data.Map
        self.Cities = self.data.mapCities
        self.directDistancePaths = self.data.mapDirectDistances
        self.searchLimited = tk.BooleanVar()
        self.searchLimited.set(False)
        self.debug = tk.BooleanVar()
        self.debug.set(DEBUG)

        # Setup GUI
        # Title Label
        labelFrame = tk.Label(self, text="Select Cities", font=LARGE_FONT)
        # OptionMenu Frame
        optionsMenuFrame = tk.Frame(self)
        # White canvas Frame
        self.canvasFrame = tk.Canvas(self, background="white")
        # Method Selector Label
        methodButtonLabel = tk.Label(self, text="Select Search Method")
        # Method Selector Frame
        methodButtonFrame = tk.Frame(self, width=50, height=20)
        # Back button Frame
        backButtonFrame = tk.Frame(self, width=50, height=40)
        # ListView - prints method iterations
        self.plotFrame = tk.Frame(self.canvasFrame, width=100)
        self.iterationList = tk.Listbox(self.canvasFrame, width=100)
        self.iterationList.bind('<<ListboxSelect>>', self.listBoxOnSelect)

        # Packing Frames
        backButtonFrame.pack(side="bottom", fill="both", expand=False)
        methodButtonFrame.pack(side="bottom")
        methodButtonLabel.pack(side="bottom")
        labelFrame.pack(side="top")
        optionsMenuFrame.pack(side="top")
        self.canvasFrame.pack(side="top", fill="both", expand=True)

        # Page Items set frames
        fromCityLabel = tk.Label(optionsMenuFrame, text="FROM")
        self.fromCityVar = tk.StringVar()  # default value
        fromCityOptionsMenu = ttk.OptionMenu(
            optionsMenuFrame, self.fromCityVar, self.Cities[0], *self.Cities)

        toCityLabel = tk.Label(optionsMenuFrame, text="TO")
        self.toCityVar = tk.StringVar()  # default value
        toCityOptionsMenu = ttk.OptionMenu(
            optionsMenuFrame, self.toCityVar, self.Cities[0], *self.Cities)

        BackBtn = ttk.Button(backButtonFrame, text="Exit", command=sys.exit)

        ClearBtn = ttk.Button(
            backButtonFrame, text="Clear Map", command=self.cleanMap)

        if (DEBUG == True):
            self.searchLimited.trace('w', lambda *_: print("Value Changed!"))
            self.debug.trace('w', lambda *_: print("Value Changed!"))

        numberCallback = (self.register(self.callbackDigit))

        self.LabelInputLimitedSearch = tk.Label(backButtonFrame, text="Levels")
        self.InputLimitedSearch = tk.Entry(
            backButtonFrame, state='disabled', validate='all', validatecommand=(numberCallback, '%P'))

        CheckBoxLimitedSearch = ttk.Checkbutton(
            backButtonFrame, text="Limited search", variable=self.searchLimited, command=self.getBool)

        CheckBoxDebugConsole = ttk.Checkbutton(
            backButtonFrame, text="Console Debug", variable=self.debug, command=self.getBool)

        IddfsBtn = ttk.Button(methodButtonFrame, text="IDDFS", command=lambda: self.setCanvasNewMap(IDDFS("Iterative Deepening Depth First Search",
                                                                                                          self.fromCityVar.get(), self.toCityVar.get(), self.Portugal, self.searchLimited.get(), self.InputLimitedSearch.get())))
        UcsBtn = ttk.Button(methodButtonFrame, text="UCS", command=lambda: self.setCanvasNewMap(UCS(
            "Uniform-Cost Search", self.fromCityVar.get(), self.toCityVar.get(), self.Portugal, self.searchLimited.get())))
        GreedyBtn = ttk.Button(methodButtonFrame, text="Greedy", command=lambda: self.setCanvasNewMap(GREEDY(
            "Greedy", self.fromCityVar.get(), self.toCityVar.get(), self.Portugal, self.searchLimited.get(), self.directDistancePaths)))
        AstarBtn = ttk.Button(methodButtonFrame, text="A*", command=lambda: self.setCanvasNewMap(ASTAR("A-Star",
                                                                                                       self.fromCityVar.get(), self.toCityVar.get(), self.Portugal, self.searchLimited.get(), self.directDistancePaths)))

        # Grid setup
        self.canvasFrame.grid_columnconfigure(0, weight=1)
        self.canvasFrame.grid_rowconfigure(0, weight=1)
        self.iterationList.grid(row=0, column=1, sticky="nsew")
        self.plotFrame.grid(row=0, column=0, sticky="nsew")
        # Clean map
        self.canvas = FigureCanvasTkAgg(
            ViewMap(self.Portugal, []).testGraph(), master=self.plotFrame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        optionsMenuFrame.grid_columnconfigure(0, weight=1)
        fromCityOptionsMenu.grid(row=0, column=1, sticky="w", padx=20)
        toCityOptionsMenu.grid(row=0, column=3, sticky="w")
        fromCityLabel.grid(row=0, column=0, sticky="w")
        fromCityLabel.grid(row=0, column=0, sticky="w")
        toCityLabel.grid(row=0, column=2, sticky="w", padx=20)

        methodButtonLabel.grid_columnconfigure(0, weight=1)
        methodButtonFrame.grid_columnconfigure(0, weight=1)
        IddfsBtn.grid(row=0, column=0, sticky="w", pady=20)
        UcsBtn.grid(row=0, column=1, sticky="w", pady=20)
        GreedyBtn.grid(row=0, column=2, sticky="w", pady=20)
        AstarBtn.grid(row=0, column=3, sticky="w", pady=20)

        backButtonFrame.grid_columnconfigure(0, weight=1)
        BackBtn.grid(row=0, column=5, sticky="e", pady=20, padx=20)
        ClearBtn.grid(row=0, column=4, sticky="e", pady=20)
        CheckBoxLimitedSearch.grid(
            row=0, column=3, sticky="e", pady=20, padx=30)
        self.InputLimitedSearch.grid(row=0, column=2, sticky="e", pady=20)
        self.LabelInputLimitedSearch.grid(row=0, column=1, sticky="e", pady=20)
        CheckBoxDebugConsole.grid(
            row=0, column=0, sticky="e", pady=20, padx=50)

    def callbackDigit(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    def getBool(self):
        if (self.debug.get() == True):
            print("Limited search: " + str(self.searchLimited.get()))
            print("Console debug: " + str(self.debug.get()))
        if self.searchLimited.get() == True:
            self.InputLimitedSearch.config(state='normal')
        else:
            self.InputLimitedSearch.config(state='disabled')

    def listBoxOnSelect(self, event):
        # Tkinter passes an event object to onselect()
        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print("Selected = {} --- {}".format(index, value))
        messagebox.showinfo(
            "Information", "Selected = {} --- {}".format(index, value))

    def clearConsole(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(os.name == 'posix')
        else:
            _ = system('clear')

    def cleanMap(self):
        self.clearConsole()
        try:
            self.canvas.get_tk_widget().pack_forget()
            self.iterationList.delete(0, 'end')
        except AttributeError:
            pass

        self.canvas = FigureCanvasTkAgg(
            ViewMap(self.Portugal, []).testGraph(), master=self.plotFrame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        matplotlib.pyplot.close('all')

    def setCanvasNewMap(self, searchMethod):
        self.cleanMap()
        try:
            self.canvas.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        self.iterationListPopulate(searchMethod.iterationList)
        self.canvas = FigureCanvasTkAgg(
            ViewMap(self.Portugal, searchMethod.selectedPath).testGraph(), master=self.plotFrame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        matplotlib.pyplot.close('all')

        if (self.debug.get() == True):
            print(searchMethod.nameMethod)
            print("From city: {} | To city: {}".format(
                self.fromCityVar.get(), self.toCityVar.get()))

    def iterationListPopulate(self, mapIterationList):
        i = 0
        for item in mapIterationList:
            self.iterationList.insert(i, item)
            if self.debug.get() == True:
                print(item)
            self.iterationList.insert(i+1, "")
            i += 2


app = Main()
matplotlib.pyplot.close('all')
app.lift()
app.attributes('-topmost', True)
app.after_idle(app.attributes, '-topmost', False)
app.mainloop()
