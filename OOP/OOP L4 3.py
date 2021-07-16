from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,40))

@dataclass
class Book:
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory = price_func)

'''
Data Classes provide the ability to define default values for attributes subject to some rules.

Doing so will allow us to create a book with no arguments. Attributes without default values must come first.

You can also import the field class to set the default for flexibility. You can also provide a function to call that provides the default value.
'''