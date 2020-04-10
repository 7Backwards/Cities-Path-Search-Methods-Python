# DepthFirstSearch
from SearchGraph import SearchGraph


class SearchGraphIDDFS(SearchGraph):

    def __init__(self, nameMethod, origin, destiny, countryMap, isLimited=True):
        super().__init__(nameMethod, origin, destiny, countryMap)
        self.isLimited = isLimited

        self.selectedPath.append(self.countryMap.pathsMap[0])
        self.selectedPath.append(self.countryMap.pathsMap[6])
        self.selectedPath.append(self.countryMap.pathsMap[8])

        self.iterationList.append("teste 1")
        self.iterationList.append("teste 2")
        self.iterationList.append("teste 3")
        self.iterationList.append("teste 4")
