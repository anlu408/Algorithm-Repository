class node:
    def __init__(self, value=None):
        self.value = value
        self.next = next #Pointer to next node

    def __str__(self):
        return str(self.value)

class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        yield curNode
        curNode = curNode.next

class circular_queue:
    def __init__(self):
        self.linked_list = linked_list()

    def __str__(self):
        values = [str(x) for x in self.linked_list]
        return ' '.join(values)

    def enqueue(self,value):
        temp_node = node(value)
        if self.linked_list.head is None:
            self.linked_list.head == temp_node
            self.linked_list.tail == temp_node
        else:
            temp_node.next = self.linked_list.tail
            self.linked_list.tail = temp_node

    def dequeue(self):
        if self.is_empty():
            print("There are no values to dequeue")
        else:
            temp_node = self.linked_list.head
            if self.linked_list.head == self.linked_list.tail:
                self.linked_list.head == None
                self.linked_list.tail == None
            else:
                self.linked_list.head = self.linked_list.head.next
            return temp_node

    def peek(self):
        if self.is_empty():
            print("There are no values to peek")
        else:
            return self.linked_list.head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None
