import matplotlib.pyplot as plt
plt.ioff()


class ViewMap():

    countryMapData = None
    pathData = None
    # Prepare nodes
    nome = []
    x = []
    y = []


    def __init__(self, countryMapData, pathData):

        self.countryMapData = countryMapData
        self.pathData = pathData
        for cols in self.countryMapData.getNodes():
            self.nome.append(str(cols.name))
            self.y.append(float(cols.lat))
            self.x.append(float(cols.lon))

    def testGraph(self):

       
        nome_onpath = []
        x_onpath = []
        y_onpath = []
        nome_offpath = []
        x_offpath = []
        y_offpath = []
        

        # Prepare lines
        for line in self.countryMapData.getEdges():

            for line1 in self.pathData:

                if line1.city1 == line.city1 and line1.city2 == line.city2:

                    self.addBlueLine(line.city1, line.city2, line.weight)
                    break

                self.addWhiteLine(line.city1, line.city2)

        if not self.pathData:
            
            plt.scatter(self.x, self.y, s=20, c='b', marker='o', label='Ports', alpha=1, zorder=1)
            for i in range(0, len(self.x)):
                
                plt.annotate(self.nome[i], xy=(self.x[i] + 0.05, self.y[i] + 0.05), size=10)
        else:
                
            for cols in self.countryMapData.getNodes():
                for line1 in self.pathData:
                    if line1.city1 == cols.name or line1.city2 == cols.name:
                        nome_onpath.append(str(cols.name))
                        y_onpath.append(float(cols.lat))
                        x_onpath.append(float(cols.lon))
                        break
                    else:
                        nome_offpath.append(str(cols.name))
                        y_offpath.append(float(cols.lat))
                        x_offpath.append(float(cols.lon))
                    
            plt.scatter(x_offpath, y_offpath, s=20, c='w', marker='o', label='Ports', alpha=1, zorder=1)
            plt.scatter(x_onpath, y_onpath, s=20, c='b', marker='o', label='Ports', alpha=1, zorder=1)
           
            for i in range(0, len(x_offpath)):
                plt.annotate(nome_offpath[i], xy=(x_offpath[i] + 0.05, y_offpath[i] + 0.05), size=10)
            for i in range(0, len(x_onpath)):
                plt.annotate(nome_onpath[i], xy=(x_onpath[i] + 0.05, y_onpath[i] + 0.05), size=10)
        
        
            
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

        # giving a title to graph
        plt.title('Cidades de Portugal')

        # function to show the plot
        # plt.show()
        fig = plt.gcf()
        return fig

    def addWhiteLine(self, cityA, cityB):

        nome = []
        x = []
        y = []

        for cols in self.countryMapData.getNodes():

            nome.append(str(cols.name))
            y.append(float(cols.lat))
            x.append(float(cols.lon))

        indexA = nome.index(cityA)
        indexB = nome.index(cityB)
        # Define lines
        x_values = [x[indexA], x[indexB]]
        y_values = [y[indexA], y[indexB]]
        # Set line
        plt.plot(x_values, y_values, 'w')

    def addBlueLine(self, cityA, cityB, weight):

        nome = []
        x = []
        y = []

        for cols in self.countryMapData.getNodes():

            nome.append(str(cols.name))
            y.append(float(cols.lat))
            x.append(float(cols.lon))

        indexA = nome.index(cityA)
        indexB = nome.index(cityB)
        # Define lines
        x_values = [x[indexA], x[indexB]]
        y_values = [y[indexA], y[indexB]]
        # Set line
        plt.plot(x_values, y_values, 'b')
        plt.text((x_values[0] + x_values[1]) / 2,
                 (y_values[0] + y_values[1]) / 2, weight, color='blue')
