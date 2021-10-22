
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    class circular_singly_linked_list:
        def __init__(self):
            self.head = None
            self.tail = None

        def __iter__(self):
            node = self.head
            while node:
                yield node

                if node.next == self.head:
                    break
                node = node.next

    def create_CSLL (self, node_value):
        node = Node(node_value)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"

    def insertion (self, value, location):
        if(self.head is None):
            return "The head reference is None"
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == -1:
                new_node.next = self.head
                self.tail.next = new_node
                self.tail = new_node
            else:
                tempNode = self.head
                index = 0
                while (index < location - 1):
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = new_node
                new_node.next = next_node
            return "The node has been successfully inserted"

    def traverse_csll(self):
        if self.head is None:
            print{"There are no elements to traverse."}
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    break
    def search_csll(self,value):
        index = 0
        if self.head is None:
            return ("There are no nodes in this circular singly linked list")
        else:
            temp_node = self.head
            while temp_node:
                if (temp_node == value):
                    return("Your value is located at: " + index)
                elif (temp_node.next == self.head):
                    return("Your value is not in the circular singly linked list")
                else:
                    temp_node = temp_node.next
                    index += 1
    def deletion (self,location):
        if self.head is None:
            print("There are no nodes in the circular singly linked list")
        else:
            if location == 0: #Delete from head
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                self.head = self.head.next
                self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    temp_node = self.head
                    while temp_node is not None:
                        if node.next == self.tail:
                            break
                        temp_node = temp_node.next
                    temp_node.next = self.head
                    self.tail = temp_node
            else:
                temp_node = self.head
                index = 0
                while temp_node:
                    while index < location - 1:
                        temp_node = temp_node.next
                        index += 1
                    new_node = temp_node.next
                    temp_node.next = new_node.next
    def delete_csll(self):
        self.head = None
        self.tail.next = None
        self.tail = None
