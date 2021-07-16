# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects

'''
Solid Book definition but it's monolithic- it's dense and there is a lot of information. It would make sense to treat these as
separate entities.
'''

class Book:
    def __init__(self, title, price, author = None):
        self.title = title
        self.price = price

        self.author = author
        self.chapters = []

    def addchapter(self, chapters): #Swap the name and pages to the class Chapter as it no longer takes name and pages
        self.chapters.append((chapters))

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        
        return result


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

auth = Author ("Leo", "Tolstoy") #Define an object named auth of the type Author to contain information about the author

b1 = Book ("War and Peace", auth, Chapter )

#b1 = Book("War and Peace", 39.0, "Leo", "Tolstoy") #Example code revised below for the two new class definitions.

'''
Define the listed chapters and pages numbers of object Chapter and then import them into the book to add the chapters for.
'''
b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.title)
print(b1.author)
print(b1.getbookpagecount())

'''
With composition you build objects out of other objects. It is more of a has relationship. The Book object has an Author object that contains info about the Author.
Rather than defining all author related information in the Book class heirarchy. This allows for distinct ideas and put them into their own classes.

While we initially had one large class that was information dense we moved first by creating a separate 
Author class that took in a first and last name and we editted the Book function to take in an Author class that defaults to None unless specified.

What follows is a separate class implementation for Chapters along with the tuple to insert more chapter information if necessary.

The addchapter function is essentially a setter function in Java and we have a getpagecount function that just
adds all of the page numbers together from the objects created in the main program. 

We made the Book class simpler by creating several smaller objects and consolidating everything in the Book class each responsible for its own features and data.
'''