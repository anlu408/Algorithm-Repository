from abc import ABC, abstractmethod
'''
Some languages have built in interfaces like Java but Python does not have built-in interfaces. Think of an interface
as a kind of promise. A class makes a contract to provide a certain kind of behavior or capibility.,
'''

class JSONIFY(ABC): #Focused class to indicate it knows how to represent itself in JSON. 

    @abstractmethod()

    def toJSON(self): #Empty implementation
        pass

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape, JSONIFY): #Requires the class to override and implement the toJSON method otherwise an error occurs
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)


c = Circle(10)
print(c.calcArea())
