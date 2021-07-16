class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __eq__(self):
        #Compares objects on an attribute by attribute basis. Should throw an exception if the object types are not the same.
        if not isinstance(value, Book): #Checks for an exception. A book object should not be compared to an item that isn't of a Book object as well.
            raise ValueError("Can't compare a book to a non-Book")
        return (self. title == value.title) and (self.author == value.author) and (self.price == value.price)

    def __ge__(self):
        if not isinstance(value, Book):
            raise ValueError("Can't compare a book to a non-Book")
        
        return self.price >= value.price

    def __lt__(self):
            if not isinstance(value, Book):
                raise ValueError("Can't compare a book to a non-Book")
            
            return self.price < value.price
    


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

'''
Plain objects by default in Python don't know how to compare stuff to each other. We can teach them how to do so with
magic comparison and equality methods. We have a book class and some objects that create Book instances.

There are two magic string functions: Str and Repr
Str- Method to return a string - Intended to be displayed to the user
Repr- Method to return an object representation - Developer facing string to recreate the object in its current state and used for debugging.

It is usually a good idea to define the repr function for classes you create to make debugging easier.

If we were to use the == operator to check for equality of b1 and b3 created with the same arguments Python would return false. This is due to the fact that
Python did not compare on an attribute by attribute basis and just compared the two instances.
'''