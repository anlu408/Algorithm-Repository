'''
There is a lot of duplication in the code below. In order to become less verbose, we can create a base class called
Publication and have that class define common attributes.
'''

class Publication:
    def __init__(self,title,price):
        self.title = title
        self.price = price
'''
Add the name of the base class into the class definition of the Book to inherit the title and price properties from the Publication
base class.
'''
class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title,price) #Call the superclass innate function and remove the self.title and self.price
        self.author = author
        self.pages = pages

class Periodical(Publication):
    def __init__(self,title,price,period,publisher):
        super().__init__(title,price)
        self.period = period
        self.publisher = publisher

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title,price,period,publisher)

class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title,price,period,publisher)


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
