class node:
    def __init__(self, value=None):
        self.value = value
        self.next = None #Pointer to next node
        self.prev = None #Pointer to previous node

    class doubly_linked_list:
        def __init__(self):
            self.head = None
            self.tail = None

        def __iter__(self):
            node = self.head
            while node:
                yield node
                node = node.next

    def create_dll (self, node_value):
        node = node(node_value)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return 'The doubly linked list has been successfully created

    def insert_node(self, node_value, location):
        if self.head is None:
            print('The node cannot be inserted')
        else:
            new_node = node(node_value)
            if location == 0:
                new_node.prev = None
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif location == -1:
                new_node.next = None
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                while (index < location - 1):
                    temp_node = temp_node.next
                    index += 1

                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node

    def traversal(self):
        if self.head == None:
            return "There are no elements in the circular doubly linked list"
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
    def reverse_traversal:
        if self.head == None:
            return "There are no elements in the circular doubly linked list"
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.prev

    def search(self, node_value):
        if self.head is None:
            "There are no elements in the doubly linked list"
        else:
            temp_node = self.head
            index = 0
            while temp_node:
                if (temp_node.value == node_value):
                    return index
                else:
                index += 1
                temp_node = temp_node.next
            return ("The value does not exist in the doubly linked list")

    def delete_node(self, location):
        if self.head is None:
            print ("There are no elements in the doubly linked list")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.tail.next = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                self.tail = self.tail.prev
                self.next = None
            else:
                index = 0
                temp_node = self.head
                while (index < location):
                    temp_node = temp_node.next
                    index += 1
                temp_node.next = temp_node.next.next
                temp_node.next.prev = temp_node
                print ("The node has been deleted")

    def delete_dll(self):
        if self.head is None:
            print("There are no elements to delete")
        else:
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
