# Greedy Search
from SearchGraph import SearchGraph


class SearchGraphGREEDY(SearchGraph):

    def __init__(self, nameMethod, origin, destiny, countryMap, isLimited, directDistanceHeuristic):
        super().__init__(nameMethod, origin, destiny, countryMap)

        self.isLimited = False

        self.directDistancePaths = directDistanceHeuristic
        self.selectedPath = []
        self.graph = {}
        self.route = []
        self.minDirectDistanceToDestiny = {}
        self.minDirectDistanceToDestiny[origin] = "0"

        for node in self.countryMap.nodesMap:
            self.graph[node.name] = []
            for path in self.countryMap.pathsMap:
                if path.city1 == node.name or path.city2 == node.name:
                    self.graph[node.name].append(path)

        self.iterationList.append("(" + origin + ")")
        # print(nameMethod)
        # print("(" + origin + ")")

        self.searchGreedy(self.graph[origin], origin,
                          destiny, origin, self.route)
        self.route.append(origin)
        self.route.reverse()
        # Alternative -> self.route(::-1)
        # print(self.route)

        count = 0
        while count < len(self.route)-1:
            for path in self.countryMap.pathsMap:
                if path.city1 == self.route[count] and path.city2 == self.route[count+1] or path.city2 == self.route[count] and path.city1 == self.route[count+1]:
                    self.selectedPath.append(path)
            count = count + 1

    def searchGreedy(self, paths, origin, destiny, currentNode, route):
        if currentNode == destiny:
            #print("Arrived - " + destiny)
            return True

        for path in paths:
            if path.city1 == currentNode:
                for directPath in self.directDistancePaths:
                    if directPath.city1 == path.city2 and directPath.city2 == destiny:
                        self.minDirectDistanceToDestiny[directPath.city1] = directPath.weight
                    elif directPath.city2 == path.city2 and directPath.city1 == destiny:
                        self.minDirectDistanceToDestiny[directPath.city2] = directPath.weight
            elif path.city2 == currentNode:
                for directPath in self.directDistancePaths:
                    if directPath.city1 == path.city1 and directPath.city2 == destiny:
                        self.minDirectDistanceToDestiny[directPath.city1] = directPath.weight
                    elif directPath.city2 == path.city1 and directPath.city1 == destiny:
                        self.minDirectDistanceToDestiny[directPath.city2] = directPath.weight

        if len(self.minDirectDistanceToDestiny) > 0:
            self.minDirectDistanceToDestiny.pop(currentNode)
            nextNode = self.getMinDirectDistanceToDestiny(
                self.minDirectDistanceToDestiny)
            # print(self.minDirectDistanceToDestiny)
            # print(nextNode)
            # print(self.minDirectDistanceToDestiny)
            if self.searchGreedy(self.graph[nextNode], origin, destiny, nextNode, route) == True:
                route.append(nextNode)
                return True

        return False

    # function to return the second element of the
    # two elements passed as the parameter
    def sortSecond(self, val):
        return val[1]

    def getMinDirectDistanceToDestiny(self, minDirectDistanceToDestiny):

        minWeight = 100000
        nextCity = ""
        nextOutPut = ""

        nextHopCandidateList = []

        for city, weight in minDirectDistanceToDestiny.items():

            nextHopCandidateList.append([city, weight])

            if int(weight) < minWeight:
                minWeight = int(weight)
                nextCity = city

        # sorts the array in ascending according to
        # second element
        nextHopCandidateList.sort(key=self.sortSecond)
        for city, weight in nextHopCandidateList:
            nextOutPut += "(" + city + ", " + weight + ")"

        self.iterationList.append(nextOutPut)
        # print(nextOutPut)
        # self.iterationList.append(str(nextHopCandidateList))
        # print(nextHopCandidateList)

        return nextCity
