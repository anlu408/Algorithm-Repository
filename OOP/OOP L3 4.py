class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    #With this function alone you can call an object and change its attributes like seen below.
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print (b1) #This will return what is listed in b1 already.

b1 = ("The Catcher in the Rye", "JD Salinger", 29.95) #This will change all of B1's values to what I transferred over from B2.