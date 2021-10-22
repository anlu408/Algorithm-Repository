class binary_tree:
    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_index = 0 #Used to make life easier when inserting
        self.max_size = size

    def insert(self, value):
        if self.last_index + 1 == max_size:
            return ("The Binary Tree is full")
        self.custom_list[self.last_index + 1] = value
        self.last_index += 1
        return ("Inserted")

    def search(self,value):
        for i in range (len(self.custom_list)):
            if self.custom_list[i] == value:
                return i #Returns index if found.
            return ("The value is not in the Binary Tree")

    def preorder_traversal(self, index): #Note that it is o(n) space complexity as we are inserting into stack memory with recurisve function calls
        if index > self.last_index:
            return
        print(self.custom_list[index])
        self.preorder_traversal(index*2)
        self.preorder_traversal(index*2 + 1)

    def in_order_traversal(self,index):
        if index > self.last_index:
            return
        self.preorder_traversal(index*2)
        print(self.custom_list[index])
        self.preorder_traversal(index*2 + 1)

    def postorder_traversal(self,index):
        if index > self.last_index:
            return
        self.preorder_traversal(index*2) #left subtree
        self.preorder_traversal(index*2 + 1) #right subtree
        print(self.custom_list[index]) #root node

    def levelorder_traversal(self,index):
        for i in range(index, self.last_index + 1)):
            print self.custom_list[i]

    def delete_node(self, value):
        if self.last_index == 0:
            return ("There are no elements in the Binary Tree")
        else:
            for i in range (1, self.last_index + 1):
                if self.custom_list[i] == value:
                    self.custom_list[i] == self.custom_list[last_index]
                    self.custom_list[self.last_index] = None
                    self.last_index -= 1
    def delete(self):
        self.custom_list = None
        return("The Binary Tree has been deleted")
