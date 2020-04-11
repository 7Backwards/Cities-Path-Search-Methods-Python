# DepthFirstSearch
from SearchGraph import SearchGraph


class SearchGraphIDDFS(SearchGraph):

	def __init__(self, nameMethod, origin, destiny, countryMap, isLimited=True):
		super().__init__(nameMethod, origin, destiny, countryMap)
		self.isLimited = isLimited

		self.limit = 20 #max iteration
		
		self.selectedPath = []

		self.graph = {}

		for node in self.countryMap.nodesMap:
			self.graph[node.name] = []
			for path in self.countryMap.pathsMap:
				if (path.city1 == node.name or path.city2 == node.name):
					self.graph[node.name].append(path)
					
		if isLimited:
			self.searchIDDFSLimited(self.graph[origin], origin, destiny, self.limit)
		else:
			self.searchIDDFSLimited(self.graph[origin], origin, destiny, self.limit)

				
				
	def searchIDDFSLimited(self, node, origin, destiny, limit):
		if origin == destiny:
			print("Path equals to destiny")
			return
		
		if len(node) > 0:
			for op in node:
				if destiny == op.city1 or destiny == op.city2:
					print("yyyyeeeeeeaaaahhhhh")
					return
		
		for item in self.graph:
			self.searchIDDFSLimited(self.graph[item], origin, destiny, limit)
			
			
		'''
		for place in self.graph:
			print(place)
			for item in self.graph[place]:
				print(item.city1 + " |  " + item.city2)
		'''

		self.selectedPath.append(self.countryMap.pathsMap[0])
		self.selectedPath.append(self.countryMap.pathsMap[6])
		self.selectedPath.append(self.countryMap.pathsMap[8])

		self.iterationList.append("teste 1")
		self.iterationList.append("teste 2")
		self.iterationList.append("teste 3")
		self.iterationList.append("teste 4")
