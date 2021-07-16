from dataclasses import dataclass #Imports data classes

@dataclass #Data class decorator
class Book:
    #self is removed as it is no longer necessary and each attribute is given the type hint instead
    title : str
    author : str
    pages : int
    price : float

    def bookinfo(self): #make sure to pass self in as an argument. This is a common mistake I make.
        return f"{self.title} by {self.author}"


# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__
print(b1)

# TODO: comparing two dataclasses - they implement __eq__
print( b1 == b2)

print(b1.bookinfo())

# TODO: change some fields

'''
The main use case for classes in Python is to contain and represent data.

Code creates classes and uses init functions to store values on instances of the class.  

The data class was introduced that automates creation and management of classes existing to just hold data.
Our book class will be converted into a data class.

For the Book class it looks like we are defining book attributes instead of instance attributes. The data class decorator will rewrite the class to automatically add the init function where each attribute is initialized on the object instance.
The type hints are required for data classes to work. Their type is not actually enforced for flexibility. Nothing needs to be changed in the main program loop as long as arguments are passed in the same order.

Data class also automatically implement repr and eq methods. 

You can add regular python methods as well.
'''