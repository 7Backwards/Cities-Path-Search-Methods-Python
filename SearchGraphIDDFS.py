# DepthFirstSearch
from SearchGraph import SearchGraph


class SearchGraphIDDFS(SearchGraph):

    def __init__(self, nameMethod, origin, destiny, countryMap, isLimited=True, limitLevel=0):
        super().__init__(nameMethod, origin, destiny, countryMap)
        self.isLimited = isLimited
        self.limit = 0

        if len(limitLevel) > 0 and len(limitLevel) < 4:
            self.limit = int(limitLevel)
        else:
            self.isLimited = False

        self.selectedPath = []
        self.graph = {}
        self.route = []
        self.visited = []
        self.tries = 0

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
        if self.isLimited:
            self.searchIDDFSLimited(
                self.graph[origin], origin, destiny, origin, self.limit, self.route)
            self.route.append(origin)
            self.route.reverse()
            # Alternative -> self.route(::-1)
            # print(self.route)

        else:
            self.searchIDDFSNotLimited(
                self.graph[origin], origin, destiny, origin, self.route, self.visited)
            self.route.append(origin)
            self.route.reverse()

        count = 0
        while count < len(self.route)-1:
            for path in self.countryMap.pathsMap:
                if path.city1 == self.route[count] and path.city2 == self.route[count+1] or path.city2 == self.route[count] and path.city1 == self.route[count+1]:
                    self.selectedPath.append(path)
            count = count + 1

        for city in self.route:
            iterationSrt = "[" + city + "]"
            for path in self.countryMap.pathsMap:
                if path.city1 == city:
                    iterationSrt = iterationSrt + ", " + path.city2
                elif path.city2 == city:
                    iterationSrt = iterationSrt + ", " + path.city1

            iterationSrt = iterationSrt + "]"
            self.iterationList.append(iterationSrt)

        self.iterationList.append("Total tries = " + str(self.tries))

    def searchIDDFSLimited(self, paths, origin, destiny, currentNode, limit, route):

        if currentNode == destiny:
            print("Arrived - " + destiny)
            return True
        elif limit == 0:
            print("Limit reached!!!")
            self.tries += 1
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

    def searchIDDFSNotLimited(self, paths, origin, destiny, currentNode, route, visited):

        visited.append(currentNode)

        if currentNode == destiny:
            print("Arrived - " + destiny)
            return True

        for path in paths:
            if path.city1 == currentNode and path.city2 not in visited:
                if self.searchIDDFSNotLimited(self.graph[path.city2], origin, destiny, path.city2, route, visited) == True:
                    route.append(path.city2)
                    return True
            elif path.city2 == currentNode and path.city1 not in visited:
                if self.searchIDDFSNotLimited(self.graph[path.city1], origin, destiny, path.city1, route, visited) == True:
                    route.append(path.city1)
                    return True

        self.tries += 1
        return False
