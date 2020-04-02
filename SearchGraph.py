
class SearchGraph:

    def __init__(self, nameMethod, origin, destiny, countryMap):
        self.nameMethod = nameMethod
        self.origin = origin
        self.destiny = destiny
        self.countryMap = countryMap
        self.selectedPath = []

    def getSelectedPath(self):
        return self.selectedPath
