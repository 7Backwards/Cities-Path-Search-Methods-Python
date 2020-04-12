# DepthFirstSearch
from SearchGraph import SearchGraph


class SearchGraphIDDFS(SearchGraph):

    def __init__(self, nameMethod, origin, destiny, countryMap, isLimited=True):
        super().__init__(nameMethod, origin, destiny, countryMap)
        self.isLimited = isLimited

        self.limit = 20
        self.selectedPath = []
        self.graph = {}
        self.route = []

        for node in self.countryMap.nodesMap:
            self.graph[node.name] = []
            for path in self.countryMap.pathsMap:
                if path.city1 == node.name or path.city2 == node.name:
                    self.graph[node.name].append(path)
        '''
        #Print all paths
        for place in self.graph:
            print(place)
            for item in self.graph[place]:
                print(item.city1 + " |  " + item.city2)
        '''
        if isLimited:         
            if self.searchIDDFSLimited(
                self.graph[origin], origin, destiny, origin, self.limit, self.route):
                self.route.append(origin)
                self.route.reverse()
                #Alternative -> self.route(::-1)
                print(self.route)

            count = 0
            while count < len(self.route)-1:
                for path in self.countryMap.pathsMap:
                    if path.city1 == self.route[count] and path.city2 == self.route[count+1] or path.city2 == self.route[count] and path.city1 == self.route[count+1]:
                        self.selectedPath.append(path)
                count = count + 1

            for city in self.route:
                self.iterationList.append(city)
                
        else:
            self.searchIDDFSNotLimited(
                self.graph[origin], origin, destiny)

    def searchIDDFSLimited(self, paths, origin, destiny, currentNode, limit, route):

        if currentNode == destiny:
            print("Arrived - " + destiny)
            return True
        elif limit == 0:
            print("Limit reached!!!")
            route.clear()
            return False

        for path in paths:
            if path.city1 == currentNode:
                if self.searchIDDFSLimited(self.graph[path.city2], origin, destiny, path.city2, limit-1, route) == True:
                    route.append(path.city2)
                    return True
            else:
                if self.searchIDDFSLimited(self.graph[path.city1], origin, destiny, path.city1, limit-1, route) == True:
                    route.append(path.city1)
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
