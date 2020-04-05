import matplotlib.pyplot as plt
plt.ion()


class ViewMap():

    countryMapData = None
    pathData = None

    def __init__(self,countryMapData,pathData):
        
        self.countryMapData = countryMapData
        self.pathData = pathData
        
    def testGraph(self):
        
        # Prepare nodes 
        nome = []
        x = []
        y= []
        
        for cols in self.countryMapData.getNodes():
            
            nome.append(str(cols.name))
            y.append(float(cols.lat))
            x.append(float(cols.lon))

        plt.scatter(x, y, s=10, c='b', marker='o',
                    label='Ports', alpha=0.65, zorder=1)
        
        for i in range(0, len(x)):
            
            plt.annotate(nome[i], xy=(x[i], y[i]), size=6)

        
        # Prepare lines
        for line in self.countryMapData.getEdges():
            
            for line1 in self.pathData:
                
                if line1.city1 == line.city1 and line1.city2 == line.city2:
                    
                    self.addBlueLine(line.city1 , line.city2 , line.weight)
                    continue
                
                self.addWhiteLine(line.city1 , line.city2)
                
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
        plt.show()


    def addWhiteLine(self,cityA,cityB):
        
        nome = []
        x = []
        y= []
        
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
        
        
    def addBlueLine(self,cityA,cityB,weight):
        
        nome = []
        x = []
        y= []
        
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
        plt.text((x_values[0] + x_values[1]) / 2 ,(y_values[0] + y_values[1]) / 2,weight,color = 'blue')

        
        
        