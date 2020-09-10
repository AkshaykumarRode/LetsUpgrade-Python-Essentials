import math
class cone:
    def __init__(self):
        radius = float(input("Enter the radius of cone: "))
        height = float(input("Enter the height of cone: "))
        self.radius = radius
        self.height = height

    def vol(self):
        volume = math.pi * (self.height/3) * (self.radius**2)
        print("Volume of cone is:",volume)

    def surf(self):
        area = math.pi * (self.radius)**2 + math.pi * self.radius* (((self.radius)**2 + (self.height)**2)**0.5)
        print("Total Surface Area is:",area)

c = cone()
c.vol()
c.surf()
