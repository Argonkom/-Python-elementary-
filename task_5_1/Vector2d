import math

class Vector2d:
    def __init__(self, x , y):
        self.x = x
        self.y = y
       
    def __add__(self, other):
        return self.x + other.x, self.y + other.y
    
    def __sub__(self, other):
        return self.x - other.x, self.y - other.y    
    
    def __mul__(self, other):
        return (self.x * other.x) + (self.y * other.y)    
    
    def dot(self, other):
        return self * other    
    
    @classmethod
    def dot1(cls, self, other):
        return (self.x * other.x) + (self.y * other.y) 

    def lengthv(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    def str(self):
        return (f"Vector has coordinates x = {self.x} and y = {self.y}")

v1 = Vector2d(1 , 2)
v2 = Vector2d(2 , 4)
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1.dot(v2))
print(Vector2d.dot1(v1, v2))
print(Vector2d.lengthv(v1, v2))
print(Vector2d.str(v2))
