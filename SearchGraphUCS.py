# UniformCostSearch
import sys
from SearchGraph import SearchGraph


class SearchGraphUCS(SearchGraph):

    def __init__(self, nameMethod, origin, destiny, countryMap, isLimited):
        super().__init__(nameMethod, origin, destiny, countryMap)
        self.isLimited = isLimited
        self.pathList = []
        self.ucs(origin, destiny,self.isLimited)
        if len(self.pathList) > 0:
            print(self.pathList)
            truePath = [destiny]
            lookForNode = destiny
            while ( lookForNode != origin):
                for path in self.pathList:
                    if lookForNode == destiny and path[1] == lookForNode:
                        
                        totalcost = path[0]
                        cost = totalcost - self.get_cost(path[1],path[2])
                        nodeBefore = path[2]
                        lookForNode = nodeBefore
                    elif path[1] == lookForNode and path[0] == cost:
                        
                        cost = cost - self.get_cost(path[1],path[2])
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
                i+=1 
            print(truePath)

        
        
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

    
    def ucs(self, origin, destiny, isLimited):
        visited = set()
        queue = []
        queue.append((0, origin))
        
        if isLimited == True:
            while len(queue) > 0:
                
                self.iterationList.append(queue.copy())
                cost, node = min(queue)
                queue.remove(min(queue))
                if node not in visited:
                    visited.add(node)
                    if node == destiny:
                        return
                    for i in self.neighbors(node):
                        if i not in visited:
                            total_cost = cost + self.get_cost(node, i)
                            queue.append((total_cost, i))
                            self.pathList.append((total_cost, i, node))     
        else:
            while len(queue) > 0:
                if len(self.pathList) == sys.maxsize:
    
                    self.iterationList.clear()
                    self.iterationList.append("Loop encontrado")
                    self.pathList.clear()
                    return  
                self.iterationList.append(str(queue.copy()))
                cost, node = min(queue)
                queue.remove(min(queue))
                if node == destiny:
                    return
                for i in self.neighbors(node):
                    total_cost = cost + self.get_cost(node, i)
                    queue.append((total_cost, i))
                    self.pathList.append((total_cost, i, node))
                    
              

