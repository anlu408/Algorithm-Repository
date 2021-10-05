'''
There are two methods to implement stacks:
List - Easier to implement, but speed problem at higher element counts
Linked List- Harder to implement, no speed problem at higher element counts.

Be careful with this method as you will have performance leak as
size grows.
'''

class Stack:
    def __init__(self):
        self.list = [] #empty stack

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return ("The element has been inserted")

    def pop (self):
        if self.is_empty():
            return "There are no elements to pop"
        else:
            return self.list.pop()

    def peek(self):
        if self.is_empty():
            return ("There are no elements to peek")
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None
