class node:
    def __init__(self, value=None):
        self.value = value
        self.next = next #Pointer to next node

class linked_list:
    def __init__(self):
        self.head = None

class stack:
    def __init__(self):
        self.linked_list = linked_list()

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def push (self,value):
        node = node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node

    def pop(self):
        if (self.head is None):
            print("There are no elements to pop")
        else:
            self.linked_list.head = self.linked_list.head.next
            print("The element has been popped")

    def peep(self):
        if self.head is None:
            print("There are no elements to peep")
        else:
            return self.linked_list.head.value

    def delete_stack(self):
        self.head = None
