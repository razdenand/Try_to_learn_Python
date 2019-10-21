from math import sqrt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def point(self):
        return ([self.x, self.y])

class Point3d(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def point(self):
        return([self.x, self.y, self.z])

def rasst3d(self, self2):
    return(sqrt((self.x - self2.x) ** 2 + (self.y - self2.y) ** 2 + (self.z - self2.z) ** 2))
def rasst2d(self, self2):
    return(sqrt((self.x - self2.x) ** 2 + (self.y - self2.y) ** 2))
