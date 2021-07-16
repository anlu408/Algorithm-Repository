class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    def __str__(self): #Overrided for a user friendly view of attributes
        return f"{self.title} by {self.author}, costs {self.price}"

    def __setattr__(self, name, value):
        if name == "price":
            if type (value) is not float:
                raise ValueError("The price attribute must be a float")
        return super().__setattr__(name,value)

    def __getattr__(self, name): #This only gets called if the get attribute version doesn't exist or if it throws an exception or if the exception does not exist.
        return name + "is not here!"

    '''
    Commented out to test getattr overwrite above. If an object is created with an attribute that doesn't exist an error will be thrown

    def __getattribute__(self, name): #This allows us to perform operations on any value before it gets returned. If you want to automatically apply the discount whenever retrieved:
        if name == "price":
            #Note that we cannot use the function call here or it will recursively call infinitely. Use the superclass version of getattribute instead.

            p = super().__getattribute__("price")
            d = super().__getattribute__("discount")

            return p - (p * d)
        #If not operating on price, just call the superclass so everything functions as usual. Add other if statements if operations must be performed on any given value.
        return super().__getattribute__(name)
'''


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)                                                                                                    

'''
Python's magic methods also give us control about how a method's attributes are accessed. We can define methods to intercept the process every time an attribute is set or retrieved
'''