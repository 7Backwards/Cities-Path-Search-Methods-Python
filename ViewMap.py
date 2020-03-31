import csv
import tkinter as tk
import sys
import matplotlib.pyplot as plt
plt.ion()


class ViewMap():

    def testGraph(self):

        # Read csv
        with open('Res/pt.csv', 'r', newline='', encoding='utf-8') as f_input:
            csv_input = csv.reader(
                f_input, delimiter=',', skipinitialspace=True)
            # ByPass header line
            next(csv_input, None)
            nome = []
            x = []
            y = []
            for cols in csv_input:
                nome.append(str(cols[0]))
                y.append(float(cols[1]))
                x.append(float(cols[2]))

        plt.scatter(x, y, s=10, c='b', marker='o',
                    label='Ports', alpha=0.65, zorder=1)
        for i in range(0, len(x)):
            plt.annotate(nome[i], xy=(x[i], y[i]), size=6)

        # Define lines
        x_values = [x[0], x[5]]
        y_values = [y[0], y[5]]
        # Set line
        plt.plot(x_values, y_values)

        # Define background image
        image = plt.imread("Res/mapa_portugal.png")
        # Define background image x and y axis range
        ext = [-9.8, -6, 36.8, 42.2]
        plt.imshow(image, zorder=0, extent=ext)
        aspect = image.shape[0]/float(image.shape[1]) * \
            ((ext[1]-ext[0])/(ext[3]-ext[2]))
        plt.gca().set_aspect(aspect)

        # Set x axis range
        plt.xlim(-9.8, -6)
        # Set y axis range
        plt.ylim(36.8, 42.2)
        # Hide x axis values
        plt.xticks([])
        # Hide y axis values
        plt.yticks([])
        # giving a title to my graph
        plt.title('Cidades de Portugal')

        # function to show the plot
        plt.show()
