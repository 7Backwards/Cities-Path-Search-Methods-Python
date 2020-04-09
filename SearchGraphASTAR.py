# AStar Search
from SearchGraph import SearchGraph


class SearchGraphASTAR(SearchGraph):

    def __init__(self, nameMethod, origin, destiny, countryMap, isLimited):
        super().__init__(nameMethod, origin, destiny, countryMap)
        self.isLimited = isLimited
