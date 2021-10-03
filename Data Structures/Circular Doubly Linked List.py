class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

    class circular_doubly_linked_list:
        def __init__(self):
            self.head = None
            self.tail = None

        def __iter__(self):
            while node:
                yield node
                node = node.next
                if node == self.tail.next:
                    break

    def create_cdll (self, node_value):
        node = Node(node_value)
        node.next = node
        node.prev = node
        self.head = node
        self.tail = node
        return "The CDLL has been created"

    def insertion (self, node_value, location):
        if self.head == None:
            print ("There are no values in the Circular Doubly Linked List")

        else:
            new_node = node(node_value)
            if location == 0:
                self.head.prev = new_node
                new_node.next = self.head
                self.head = new_node
                self.head.prev = self.tail
                self.tail.next = new_node
            elif location == -1:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
                self.head.prev = new_node
                self.tail.next = self.head
            else:
            temp_node = self.head
            index = 0
            while (index < location - 1):
                temp_node = temp_node.next
                index += 1
            new_node.prev = temp_node
            new_node.next = temp_node.next
            temp_node.next.prev = new_node
            temp_node.next = new_node
            return ("The node has been inserted")

    def traversal (self):
        if (self.head is None):
            print("There are no elements to traverse")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node)
                if(temp_node == self.tail):
                    break
                temp_node = temp_node.next
    def reverse_traversal (self):
        if self.head is None:
            print ("There are no elements to traverse")
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node)
                if(temp_node == self.head):
                    break
                temp_node = temp_node.prev

    def search(self, value):
        if self.head is None:
            print("There are no elements to search for in the circular doubly linked list")
        else:
            index = 0
            temp_node = self.head

            while temp_node:
                if (temp_node = value):
                    print(index)
                elif (temp_node = self.tail):
                    return ("The value is not in the circular doubly linked list")
                else:
                    temp_node = temp_node.next
                    index += 1
    def delete_node(self, location):
        if self.head is None:
            print("There are no elements to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head.next.prev = self.tail
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail.prev.next = self.head
                    self.tail = self.tail.prev
                    self.head.prev = self.tail
            else:
                index = 0
                temp_node = self.head
                while (index < location - 1):
                    temp_node = temp_node.next
                temp_node.next = temp_node.next.next
                temp_node.next.prev = temp_node
                print("The node has been deleted")
    def delete_cdll(self):
        if self.head is None:
            print("There are no elements to delete")
        else:
            self.tail.next = None
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
            print("The circular doubly linked list has been deleted")
