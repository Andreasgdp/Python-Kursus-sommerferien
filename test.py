import math

class Vector:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z


  @classmethod
  def stedvektor(cls, p):

    return cls(p.x, p.y, p.z)

  def length(self):
    l = math.sqrt(self.x**2 + self.y**2 + self.z**2)
    l = "{:10.2f}".format(l)

    return float(l)

v1 = Vector(1, 2, 3)

længden = v1.length()

v2 = v1.stedvektor()

print(v2)

v2.length()