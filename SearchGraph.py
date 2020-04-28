

class SearchGraph:

    def __init__(self, debug, nameMethod, origin, destiny, countryMap):
        self.nameMethod = nameMethod
        self.origin = origin
        self.destiny = destiny
        self.countryMap = countryMap
        self.selectedPath = []
        self.iterationList = []
