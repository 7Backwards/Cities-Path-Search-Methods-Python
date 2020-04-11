# DepthFirstSearch
from SearchGraph import SearchGraph


class SearchGraphIDDFS(SearchGraph):

    def __init__(self, nameMethod, origin, destiny, countryMap, isLimited=True):
        super().__init__(nameMethod, origin, destiny, countryMap)
        self.isLimited = isLimited

        self.limit = 20
        self.selectedPath = []
        self.graph = {}

        for node in self.countryMap.nodesMap:
            self.graph[node.name] = []
            for path in self.countryMap.pathsMap:
                if (path.city1 == node.name or path.city2 == node.name):
                    self.graph[node.name].append(path)

        if isLimited:
            self.searchIDDFSLimited(
                self.graph[origin], origin, destiny, self.limit)
        else:
            self.searchIDDFSNotLimited(
                self.graph[origin], origin, destiny)

    def searchIDDFSLimited(self, node, origin, destiny, limit):
        if origin == destiny:
            print("Path equals to destiny")
            return True
        elif limit == 0:
            print("Fail - limit 0")
            return False

        for op in node:
            if destiny == op.city1 or destiny == op.city2:
                print("yyyyeeeeeeaaaahhhhh")
                return True

        for item in self.graph:
            if self.searchIDDFSLimited(self.graph[item], origin, destiny, limit-1) == True:
                return True

        return False

    def searchIDDFSNotLimited(self, node, origin, destiny):
        if origin == destiny:
            print("Path equals to destiny")
            return True

        for op in node:
            if destiny == op.city1 or destiny == op.city2:
                print("yyyyeeeeeeaaaahhhhh")
                return True

        for item in self.graph:
            if self.searchIDDFSLimited(self.graph[item], origin, destiny) == True:
                return True

        return False
