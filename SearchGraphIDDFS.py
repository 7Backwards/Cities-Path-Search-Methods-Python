# DepthFirstSearch
from SearchGraph import SearchGraph


class SearchGraphIDDFS(SearchGraph):

    def __init__(self, nameMethod, origin, destiny, countryMap, isLimited):
        super().__init__(nameMethod, origin, destiny, countryMap)
        self.isLimited = isLimited

        self.limit = 5
        self.selectedPath = []
        self.graph = {}
        route = []

        for node in self.countryMap.nodesMap:
            self.graph[node.name] = []
            for path in self.countryMap.pathsMap:
                if (path.city1 == node.name or path.city2 == node.name):
                    self.graph[node.name].append(path)
        '''
        for place in self.graph:
            print(place)
            for item in self.graph[place]:
                print(item.city1 + " |  " + item.city2)
        '''
        if isLimited:
            self.searchIDDFSLimited(
                self.graph[origin], origin, destiny, origin, self.limit, route)
        else:
            self.searchIDDFSNotLimited(
                self.graph[origin], origin, destiny)

    def searchIDDFSLimited(self, paths, origin, destiny, currentNode, limit, route):
        if currentNode not in route:
            route.append(currentNode)
            print(currentNode)

        if currentNode == destiny:
            print("Arrived - " + destiny)
            print(route)
            return True
        elif limit == 0:
            print("Limit reached!!!")
            route.clear()
            route.append(origin)
            return False

        for path in paths:
            if path.city1 == currentNode:
                if self.searchIDDFSLimited(self.graph[path.city2], origin, destiny, path.city2, limit-1, route) == True:
                    return True
            else:
                if self.searchIDDFSLimited(self.graph[path.city1], origin, destiny, path.city1, limit-1, route) == True:
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
