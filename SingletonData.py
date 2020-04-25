from CountryMap import CountryMap
from CityNode import CityNode
from PathEdge import PathEdge
import csv


class SingletonData:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(SingletonData, cls).__new__(cls)
            cls.Map = CountryMap("Mapa de Portugal")
            cls.mapCities = []
            cls.mapDirectDistances = []

            # Read csv
            with open('Res/pt.csv', 'r', newline='', encoding='utf-8') as f_input:
                csv_input = csv.reader(
                    f_input, delimiter=',', skipinitialspace=True)
                # ByPass header line
                next(csv_input, None)

                for cols in csv_input:
                    tempNode = CityNode(cols[0], cols[1], cols[2])
                    cls.Map.addNode(tempNode)

            with open('Res/arestas.csv', 'r', newline='', encoding='utf-8') as f_input:
                csv_input = csv.reader(
                    f_input, delimiter=',', skipinitialspace=True)
                # ByPass header line
                next(csv_input, None)

                for cols in csv_input:
                    tempPath = PathEdge(cols[0], cols[1], cols[2])
                    cls.Map.addPath(tempPath)
            # cls.Map.printPaths()

            with open('Res/directDistanceBetweenCities.csv', 'r', newline='', encoding='utf-8') as f_input:
                csv_input = csv.reader(
                    f_input, delimiter=',', skipinitialspace=True)
                # ByPass header line
                next(csv_input, None)

                for cols in csv_input:
                    if cols[1] not in cls.mapCities:
                        cls.mapCities.append(cols[1])

                    tempPath = PathEdge(cols[0], cols[1], cols[2])
                    cls.mapDirectDistances.append(tempPath)

            '''
            for item in cls.mapDirectDistances:
                print(item.city1 + "|" + item.city2 + "|" + item.weight)
            '''

        return cls._instance
