'''
A linked list is a data structure contianing a head, tail and length property.
Linked Lists consists of nodes with each having a value and a pointer to another
node or null(if it is the last element in the list)

The term Singly comes from the fact that each node is SINGLY connect
to the next node. A doubly linked list points in both directions.

SLL's do not have indexs and do not allow for random access. They are mainly for
when you care about inserting and deleting and you just need to store a lot of
information and you don't need to randommly access the data.

A linked list is a collection of nodes so define a collection of nodes where
each stores a piece of data and a reference to the next node.

Insertion
--------------------------------------------------------------------------------
There are three scenarios that can occur when inserting into the SLL.

You can insert in the beginning of the list, insert in the middle of the list
and insert at the end of the list.

When inserting in the beginning of the list you can just edit the SLL so that
the head is the new node that you create and set the next value to point to the
previous head.

When inserting into the middle of the SLL, take the previous node and have the
next value point to the new node, and have the new node point to the next value
that the previous node pointed to.

When inserting at the end of the SLL, first set the next value of the current
tail and set that equal to the new node. After this, you can set the SLL's tail
to point to the value that you inserted as the tail.

Traversal
--------------------------------------------------------------------------------
'''

class node:
    def __init__(self, value=None):
        self.value = value
        self.next = None #Pointer to next node

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self,value,location):
        newNode = Node(value)
        if(self.head is None):
            self.head = newNode
            self.tail = newNode
        #Insert at head
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            #Insert at tail
        elif location == -1: #Use -1 here to insert at tail.
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            #Insert in middle
            else:
                tempNode = self.head
                index = 0
                while (index < location - 1):
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode
    #SLL traversal
    def traversal(self):
        if self.head is None:
            print{"The Singly Linked List does not exist."}
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next


    def SearchSLL(self, nodeValue):
        if self.head is None:
            print("The Singly Linked List does not exist")

        else:
            index = 0 #Index for location of node value
            node = self.head
            #While loop traverses SLL and if the value is found, the node value and index in the SLL is returned.
            while node is not None:
                if(nodeValue == node.value):
                    print("The value: ", nodeValue, "is found at position ", index ,  "in the Singly Linked List")
                elif(node.next is None): #If at the tail we have not found the value, we know that it is not in the Singly Linked List
                    print("The value is not in the Singly Linked List")
                    break
                node = node.next
                index += 1
            return "The value does not exist in this list"

    def deleteNode(self,location):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            #If location is 0, delete the head, 1, delete the tail.
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1: #Need to use -1 here.
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                next_node = tempNode.nextif
                tempNode.next = next_node.next
    def deleteSLL(self):
        if self.head = None:
            print("The Singly Linked List does not exist")
        else:
            self.head = None
            self.tail = None






'''
Example for the above: you have an SLL:
1->2->4->5 1 is element 0, 2 is element 1...etc.

If we want to insert 3 between 2 and 4 we insert at location 2.
tempNode is first set to 2 and this causes nextNode to be set to 4.
the next line of code makes node with the value 2 point towards the newNode 3
next. Then the last step is to just set out newNode (3) to point to the
next node 4.
'''



singlyLinkedList = SLL()
print([node.value for node in singlyLinkedList])
