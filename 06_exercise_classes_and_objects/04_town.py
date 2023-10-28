class Town:
    latitude = 0
    longitude = 0

    def __init__(self, name: str):
        self.name = name

    def set_latitude(self, latitude):
        # sets an latitude
        Town.latitude = latitude

    def set_longitude(self, longitude):
        # sets an longitude
        Town.longitude = longitude

    def __repr__(self):
        # returns an representation of the object
        return f"Town: {self.name} | Latitude: {Town.latitude} | Longitude: {Town.longitude}"


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
