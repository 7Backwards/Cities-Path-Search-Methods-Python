# UniformCostSearch
import sys
from SearchGraph import SearchGraph


class SearchGraphASTAR(SearchGraph):

    def __init__(self, debug, nameMethod, origin, destiny, countryMap, isLimited, directDistanceHeuristic):
        super().__init__(debug, nameMethod, origin, destiny, countryMap)
        self.directDistancePaths = directDistanceHeuristic
        self.isLimited = isLimited
        self.pathList = []
        self.iterationList = []
        self.astar(debug, origin, destiny, self.isLimited)
        if len(self.pathList) > 0:
            # print(self.pathList)
            truePath = [destiny]
            lookForNode = destiny
            while (lookForNode != origin):
                for path in self.pathList:
                    if lookForNode == destiny and path[1] == lookForNode:

                        totalcost = path[0]
                        cost = totalcost - self.get_cost(path[1], path[2])
                        nodeBefore = path[2]
                        lookForNode = nodeBefore
                    elif path[1] == lookForNode and path[0] == cost:

                        cost = cost - self.get_cost(path[1], path[2])
                        node = path[1]
                        nodeBefore = path[2]
                        lookForNode = nodeBefore
                        break
                truePath.append(lookForNode)
            truePath.reverse()
            i = 0
            for i in range(0, len(truePath) - 1):
                for pathMap in self.countryMap.getEdges():
                    if (truePath[i] == pathMap.city1 and truePath[i+1] == pathMap.city2) or (truePath[i] == pathMap.city2 and truePath[i+1] == pathMap.city1):
                        self.selectedPath.append(pathMap)
                i += 1
            self.formatIterationList()

    def neighbors(self, node):

        edges = []
        for edge in self.countryMap.getEdges():

            if node == edge.city1:

                edges.append(edge.city2)
            elif node == edge.city2:

                edges.append(edge.city1)

        return edges

    def get_cost(self, from_node, to_node):

        for edge in self.countryMap.getEdges():

            if (from_node == edge.city1 and to_node == edge.city2) or (from_node == edge.city2 and to_node == edge.city1):

                return int(edge.weight)

        return None

    def get_cost_to_destiny(self, from_node, to_node):

        for directPath in self.directDistancePaths:

            if (from_node == directPath.city1 and to_node == directPath.city2) or (from_node == directPath.city2 and to_node == directPath.city1):

                return int(directPath.weight)

        return None

    def formatIterationList(self):

        newIterationItem = []
        newIterationList = []
        counter = 0
        for item in self.iterationList:

            if counter != len(self.iterationList) - 1:
                for i in item:

                    newIterationItem.append(
                        str(i[2]) + "[" + str(i[1]) + "+" + str(i[0] - i[1]) + "]=" + str(i[0]))
                newIterationList.append(str(newIterationItem.copy()))
                newIterationItem.clear()
            else:
                newIterationList.append(str(item))
            counter += 1

        self.iterationList = newIterationList.copy()

    def astar(self, debug, origin, destiny, isLimited):

        visited = set()
        queue = []
        queue.append((self.get_cost_to_destiny(origin, destiny), 0, origin))

        if isLimited == True:
            while len(queue) > 0:

                # Print here
                if debug == True:
                    print(queue.copy())
                self.iterationList.append(queue.copy())
                cost_to_destiny, cost, node = min(queue)
                queue.remove(min(queue))
                if node not in visited:
                    visited.add(node)
                    if node == destiny:
                        if origin != destiny:
                            queue.clear()
                            queue.append((cost, destiny))
                            self.iterationList.append(str(queue.copy()))
                        return
                    for i in self.neighbors(node):
                        if i not in visited:
                            total_cost = cost + self.get_cost(node, i)
                            cost_to_destiny = total_cost + \
                                self.get_cost_to_destiny(i, destiny)
                            queue.append((cost_to_destiny, total_cost, i))
                            self.pathList.append((total_cost, i, node))
        else:
            while len(queue) > 0:

                # Print here
                if debug == True:
                    print(queue.copy())
                self.iterationList.append(queue.copy())
                cost_to_destiny, cost, node = min(queue)
                queue.remove(min(queue))
                if node == destiny:
                    if origin != destiny:
                        queue.clear()
                        queue.append((cost, destiny))
                        self.iterationList.append(str(queue.copy()))
                    return
                for i in self.neighbors(node):
                    total_cost = cost + self.get_cost(node, i)
                    cost_to_destiny = total_cost + \
                        self.get_cost_to_destiny(node, destiny)
                    queue.append((cost_to_destiny, total_cost, i))
                    self.pathList.append((total_cost, i, node))
