class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        # returns the circumference of the circle
        circumference = Circle.__pi * self.diameter
        return circumference

    def calculate_area(self):
        # returns the area of the circle
        area = Circle.__pi * (self.diameter / 2) ** 2
        return area

    def calculate_area_of_sector(self, angle_pos):
        # gives the central angle in degrees, returns the area that fills the sector
        area_of_one_sector = (angle_pos / 360) * Circle.__pi * (self.diameter / 2) ** 2
        return area_of_one_sector


# object
circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
