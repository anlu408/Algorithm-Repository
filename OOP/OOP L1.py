class Book:
    def __init__(self, title, author, pages, price, booktype):
        self.title = title
        self.pages = pages
        self.price = price

        if(not booktype in Book.BOOK_TYPES):
            raise ValueError (f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype
    
    def getprice(self):
        if hasattr(self, "_discount"): #Checks if the discount attribute is present
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK") #properties defined at the class level are shared by all instances

    @classmethod
    def getbooktypes(cls): #works on a class instance, not an object instance
        return cls.BOOK_TYPES

    #Accessing the class attribute
    print("Book Types: ", Book.getbooktypes())


    #Double underscore properties are hidden from other classes- essentially a private variable
    __booklist = None

    #Static methods: different in that they don't modify the instance of the class or object instance. Useful for scenarios where you don't need to access the object or class itself
    #or it makes sense for it to belong the class. Good for namespacing certain methods instead of a global function.

    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        else: 
            return Book.__booklist

    #The underscore is to tell other developers using this class a hint that this attribute is internal to the class and should not be accessed from outside the class' logic
    def setdiscount(self,amount):
        self._discount = amount

#Create instances of the class
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95) #Creates an instance of Book named b1.


'''
When a class is created the init function is called to initialize the new object with information. In this case it is title and it is called before any other function
#defined in the class. Note that this isn't a constructor, initializer is more correct that constructor.

Adding the argument in the title sets the book's title to whatever is passed as the argument.

Note that despite the class taking two arguments only one is provided during instance creation
#Whenever a method is called on a python object, the object itself is automatically passed in as the first argument.
#Self is a naming convention and it is standard to use self.

the keyword type will tell what type an object is. i.e. if you run type(b1) you will get told that b1 is of type book. You can use it to compare objects to see if they are the same type. 
#You can use isinstance to check if an object is of a certain type i.e. print(isinstance(b1,book)) would return true because b1 is a book
'''