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

    def getMaoName(self):
        return self.mapName
