'''
Notes
BST- Only using LL here.
- In left subtree, value of node is less than or equal to parent node value
- In right subtree, value of node is greater than or equal to parent node value

Uses implicit structure to keep track of where elements are and performs faster
than binary trees when inserting and deleting nodes.

Common operations: Creation, Insertion, Deletion of Node, Searching, Traversing, Deletion of entire BST
'''
class bst_node(self, data):
    self.data = data
    self.left_child = None
    self.right_child = None

    def insert(root_node,value):
        if root_node is None:
            root_node.data = node_value

        elif value <= root_node.data:
            if root_node.left_child is None:
                root_node.left_child = bst_node(value)
            else:
                insert_node(root_node.left_child, value)

        else value >= root_node.data:
            if root_node.right_child is None:
                root_node.right_child = bst_node(value)
            else:
                insert_node(root_node.right_child, value)
        return ("Successfully inserted")

    def preorder_traversal(root_node):
        if not root_node:
            return
        print(root_node.data)
        preorder_traversal(root_node.left_child)
        preorder_traversal(root_node.right_child)

    def inorder_traversal(root_node):
        if not root_node:
            return
        inorder_traversal(root_node.left_child)
        print(root_node.data)
        inorder_traversal(root_node.right_child)

    def postorder_traversal(root_node):
        if not root_node:
            return
        postorder_traversal(root_node.left_child)
        postorder_traversal(root_node.right_child)
        print(root_node.data)

    def levelorder_traversal(root_node):
        if not root_node:
            return
        else:
            while not (custom_queue.isempty()):
                root = custom_queue.dequeue()
                print(root.value.data)
                if root.value.left_child is not None:
                    custom_queue.enqueue(root_node.value.data)
                if root.value.right_child is not None:
                    custom_queue.enqueue(root_node.value.data)
    def search_bst(root_node, value):
        if root_node.data == value:
            return ('The value is found')
        elif value < root_node.data:
            if root_node.left_child.data == value:
                return("The value is found")
            else:
                search_bst(root_node.left_child, value)
        elif value > root_node.data:
            if root_node.right_child.data == value:
                return ("The value is found")
            else:
                search_bst(root_node.right_child, value)
    #Helper to delete node
    def minimum_value(root_node):
    temp = bst_node
    while(current.left_child is not None):
        current = current.left_child
    return current

    def delete_node(root_node, value):
        #Base case
        if root_node is None:
            return root_node
        if value < root_node.data:
            #Traverses left side of tree if value is smaller than root node
            root_node.left_child = delete_node(root_node.left_child, value)
        elif value > root_node.data:
            #Traverses right side of tree if value is larger than root node
            root_node.right_child = delete_node(root_node.right_child, value)
        #Case 2: Node with one child
        else:
            #If there is no left child, there is a right child.
            if root_node.left_child is None:
                temp = root_node.right_child
                root_node = None
                return temp
            #If no right child, there is a left child
            if root_node.right_child is None:
                temp = root_node.left_child
                root_node = None
                return temp
            #Case 3: Node with two children
            #With two children, node with minimum value of right side of tree is set to root node. Then recursive function call to delete the minimum value.
            temp = minimum_value(root_node.right_child):
            root_node.data = temp.data
            root_node.right_child = delete_node(root_node.right_child, temp.data)
        return root_node

    def delete_bst(root_node):
        root_node = None
        root_node.left_child = None
        root_node.right_child = None
