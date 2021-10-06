class queue:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in self.list]
        return ' '.join(values)

    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False

    def enqueue(self,value):
        self.list.append(value)
        return ("The value has been added to the queue")

    def dequeue(self):
        if self.list is None:
            return ("There are no values in the queue to dequeue")
        else:
            return self.list.pop(0)

    def peek(self):
        if self.list is None:
            return ("There are no values in the queue")
        else:
            return self.list[0]

    def delete(self):
        self.list = None
