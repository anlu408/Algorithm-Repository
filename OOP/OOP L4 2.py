from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float


    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"


#Book object intitialization
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

'''
Post-Init functions will also us to additional object initialization if the data class writes the init class for you.
We can't write init as the data class does it for you. To work around this we can use post_init and is called for you after the init function is finished.

This is typically used for other attributes that depend on the value of previously existing attributes when using data classes.
'''