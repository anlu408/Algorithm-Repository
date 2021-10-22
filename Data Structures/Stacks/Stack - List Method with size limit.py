class Stack:
    def __init__(self, size):
        self.max_size = size
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

    def is_full(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False

    def push(self, value):
        if self.is_full():
            return ("The stack is full")

        else:
            self.list.append(value)
            return ("The element has been inserted")

    def pop(self):
        if self.is_empty():
            return ("There are no elements to pop")
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return ('There are no elements to peek')
        else:
            return self.list([len(self.list)] - 1)

    def delete(self):
        self.list = None
