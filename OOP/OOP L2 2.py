'''
We want to be able to create a base class and for anyone coding to not create an object of this base class as it's supposed to be a blueprint for other classes.
You want to enforce the constraint that there are certain methods in the base class that the subclasses have to implement. This is where abstract base base classes become
useful.

We want Circle and Square to implement GraphicShape so that the area must be calculated but also prevent any object of the type GraphicShape from being instantiated.
'''

from abc import ABC, abstractmethod


class GraphicShape(ABC): #Adding (ABC) turns GraphicShape into an abstract base class
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self): #calcArea becomes an abstract method. There is no implementation in the base class and each subclass has to override the method. Don't forget that you must pass self into an abstract method.
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    
    def calcArea(self):
        return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    
    def calcArea(self):
        return (self.side * self.side)


#g = GraphicShape()

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
