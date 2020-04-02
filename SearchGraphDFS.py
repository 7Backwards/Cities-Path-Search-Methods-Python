# DepthFirstSearch
from SearchGraph import SearchGraph


class SearchGraphDFS(SearchGraph):

    def __init__(self, nameMethod, origin, destiny, countryMap, isLimited=True):
        super().__init__(self, nameMethod, origin, destiny, countryMap)
        self.isLimited = isLimited
