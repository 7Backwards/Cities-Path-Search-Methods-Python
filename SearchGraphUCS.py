# UniformCostSearch
from SearchGraph import SearchGraph
from queue import Queue, PriorityQueue


class SearchGraphUCS(SearchGraph):

    def __init__(self, nameMethod, origin, destiny, countryMap, isLimited):
        super().__init__(nameMethod, origin, destiny, countryMap)
        self.isLimited = isLimited
        self.ucs(origin, destiny)

        # self.selectedPath.append(self.countryMap.pathsMap[0])
        # self.selectedPath.append(self.countryMap.pathsMap[6])
        # self.selectedPath.append(self.countryMap.pathsMap[8])
        
        
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


    def ucs(self, origin, destiny):
        visited = set()
        queue = []
        queue.append((0, origin))
        
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
        

