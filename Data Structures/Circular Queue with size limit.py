def queue:

    def __init__(self, size):
        self.items = size * [None]
        self.size = size
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def is_full(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.size:
            return True
        else:
            return False

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue (self, value):
        if self.is_full(): #Checks for full queue
            return "The queue is full"
        else:
            '''
            If top is located at the end of the queue and the queue is not full,
            an element has been dequeued. Dequeueing only pops the first element,
            this allows us to place the next enqueued element at the start
            of the list. However, this is fine because we have tracked
            the start of the queue.
            '''
            if self.top + 1 == self.size:
                self.top = 0
            else:
                #if top is not full and not at the end of the list, we add as normal
                self.top += 1
                #For empty queues
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value

    def dequeue(self):
        if self.is_full():
            return "The queue is full"
        else:
            first_element = self.items[self.start] #Element # of start.
            start = self.start
            if self.start == self.top: #Checks if this is the only element in the queue
                self.start = -1
                self.top = -1
            elif (self.start + 1 == self.size):
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return first_element

    def peek (self):
        if self.is_empty():
            return ("There are no elements in the queue")
        else:
            return self.item[self.start]

    def delete(self):
        self.items = self.size * [None]
        self.top = -1
        self.start = -1
