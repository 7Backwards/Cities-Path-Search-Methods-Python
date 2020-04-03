from CountryMap import CountryMap
from CityNode import CityNode
from PathEdge import PathEdge
import csv


class SingletonData:

    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super(SingletonData, self).__new__(self)
            self.Map = CountryMap("Mapa de Portugal")
            self.mapCities = []
            self.distToFaro = {}

            # Read csv
            with open('Res/pt.csv', 'r', newline='', encoding='utf-8') as f_input:
                csv_input = csv.reader(
                f_input, delimiter=',', skipinitialspace=True)
                # ByPass header line
                next(csv_input, None)

                for cols in csv_input:
                    tempNode = CityNode(cols[0], cols[1], cols[2])
                    self.Map.addNode(tempNode)
            

            with open('Res/arestas.csv', 'r', newline='', encoding='utf-8') as f_input:
                csv_input = csv.reader(
                    f_input, delimiter=',', skipinitialspace=True)
                # ByPass header line
                next(csv_input, None)

                for cols in csv_input:
                    tempPath = PathEdge(cols[0], cols[1], cols[2])
                    self.Map.addPath(tempPath)
            # self.Map.printPaths()

            with open('Res/dist2Faro.csv', 'r', newline='', encoding='utf-8') as f_input:
                csv_input = csv.reader(
                    f_input, delimiter=',', skipinitialspace=True)
                # ByPass header line
                next(csv_input, None)

                for cols in csv_input:
                    self.mapCities.append(cols[0])
                    self.distToFaro[cols[0]] = cols[1]
                # print(self.distToFaro)
        return self._instance
    
        
        




    