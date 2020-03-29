# Composite class Map


class CountryMap:

    def __init__(self, mapName):
        self.mapName = mapName
        self.nodesMap = []
        self.pathsMap = []

    def addNode(self, attr):
        if attr not in self.nodesMap:
            self.nodesMap.append(attr)

    def deleteNode(self, attr):
        if attr in self.nodesMap:
            self.nodesMap.remove(attr)

    def addPath(self, attr):
        if attr not in self.pathsMap:
            self.pathsMap.append(attr)

    def deletePath(self, attr):
        if attr in self.pathsMap:
            self.pathsMap.remove(attr)

    def clearNodes(self):
        self.nodesMap.clear()

    def clearPaths(self):
        self.pathsMap.clear()

    def getMapName(self):
        return self.mapName

    def getNodes(self):
        return self.nodesMap

    def getEdges(self):
        return self.pathsMap

    def printNodes(self):
        for node in self.nodesMap:
            print("City: {}\tLatitude: {}\tLongitude: {}".format(
                node.getName(), node.getLatitude(), node.getLongitude()))

    def printPaths(self):
        for path in self.pathsMap:
            print("City 1: {}\t\tCity 2: {}\t\tWeight: {}".format(
                path.getCity1(), path.getCity1(), path.getWeight()))
