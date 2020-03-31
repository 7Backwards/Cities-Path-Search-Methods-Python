# Node class


class CityNode():

    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def getName(self):
        return self.name

    def getLatitude(self):
        return self.lat

    def getLongitude(self):
        return self.lon
