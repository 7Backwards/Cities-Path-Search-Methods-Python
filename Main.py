import sys
import matplotlib.pyplot as plt; plt.ion()

import tkinter as tk
import csv

from tkinter import ttk

LARGE_FONT = ("Verdana", 12)


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, *kwargs)

        if sys.platform.startswith('win'):
            tk.Tk.iconbitmap(self, default='favicon.ico')

        tk.Tk.wm_title(self, "IA - Search Methods")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, OptionsPage, MapPage):
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
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Options",
                             command=lambda: controller.show_frame(OptionsPage))
        button1.pack()

        button2 = ttk.Button(self, text="Map",
                             command=lambda: controller.show_frame(MapPage))
        button2.pack()


class OptionsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Options Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to start menu",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()


def testGraph():
    
    #Read csv
    with open('pt.txt','r') as f_input:
        csv_input = csv.reader(f_input, delimiter=',', skipinitialspace=True)
        nome = []
        x = []
        y = []
        for cols in csv_input:
            nome.append(str(cols[0]))
            y.append(float(cols[1]))
            x.append(float(cols[2]))


    plt.scatter(x, y, s=10, c='b', marker='o', label = 'Ports',alpha=0.65, zorder=1)
    for i in range (0,len(x)):
        plt.annotate(nome[i],xy=(x[i],y[i]),size=6)

    #Define lines
    x_values = [x[0], x[5]]
    y_values = [y[0], y[5]]
    #Set line
    plt.plot(x_values, y_values)

    #Define background image
    image = plt.imread("mapa_portugal.png")
    #Define background image x and y axis range
    ext = [-9.8, -6, 36.8, 42.2]
    plt.imshow(image, zorder = 0, extent = ext)
    aspect=image.shape[0]/float(image.shape[1])*((ext[1]-ext[0])/(ext[3]-ext[2]))
    plt.gca().set_aspect(aspect)
    
    #Set x axis range
    plt.xlim(-9.8,-6)
    #Set y axis range
    plt.ylim(36.8,42.2)
    #Hide x axis values
    plt.xticks([])
    #Hide y axis values
    plt.yticks([])
    # giving a title to my graph 
    plt.title('Cidades de Portugal')

    # function to show the plot
    plt.show()




class MapPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Map Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to start menu",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="test graph",
                             command=lambda: testGraph())
        button2.pack()


app = Main()
app.mainloop()
