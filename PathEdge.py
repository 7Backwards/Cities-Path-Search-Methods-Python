# Edge class


class PathEdge():

    def __init__(self, city1, city2, weight):
        self.city1 = city1
        self.city2 = city2
        self.weight = weight

    def getCity1(self):
        return self.city1

    def getCity2(self):
        return self.city2

    def getweight(self):
        return self.weight
