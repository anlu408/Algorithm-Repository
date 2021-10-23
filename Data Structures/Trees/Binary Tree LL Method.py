'''
Binary Trees have at most two children referred to as left and right

Huffman coding problem, heap priority, expression parsing can be solved
with binary trees
Full binary tree- all leafs are either empty or full
Perfect Bianry Tree- all leafs have two children
Complete Binary Tree- All levels filled except last level
Balanced Binary Tree- Each leaf is not more than a certain distance from the root node. All leaf nodes are the same distance from the root.

Two types of Binary Tree:
-Linked List
-Python List

Depth First Search
Preorder Traversal- Root -> Left -> Right visit all nodes until no more left nodes then move right
Inorder Traversal- Left -> Root -> Right visit all nodes until no more left then move to right and move right
Postorder Traversal- Left->Right->Root

Breadth first search
Level Order Traversal-
'''

def tree_node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def preorder_traversal(root_node):
        if not root_node:
            return
        print(root_node.data)
        preorder_traversal(root_node.left_child)
        preorder_traversal(root_node.right_child)

    def inorder_traversal(root_node):
        if not root_node:
            return
        print(root_node.data)
        in_order_traversal(root_node.left_child)
        print(root_node.data)
        in_order_traversal(root_node.right_child)

    def postorder_traversal(root_node):
        if not rootnode:
            return
        in_order_traversal(root_node.left_child)
        in_order_traversal(root_node.right_child)
        print(root_node.data)

    def levelorder_traversal(root_node):
        if not root_node:
            return
        else:
            custom_queue = queue.queue()
            custom_queue = enqueue(root_node)
            while not (custom_queue.isempty()):
                root = custom_queue.dequeue()
                print(root.value.data)
                if root.value.left_child is not None:
                    custom_queue.enqueue(root_node.value.data)
                if root.value.right_child is not None:
                    custom_queue.enqueue(root_node.value.data)
                    
    def search_bt(root_node, value):
        if not root_node:
            return
        else:
            custom_queue = queue.queue()
            custom_queue.enqueue(root_node)
            while not (custom_queue.isempty()):
                root = custom_queue.dequeue()
                if root.value.data == value:
                    return "Success"
                if root.value.left_child is not None:
                    custom_queue.enqueue(root_node.value.data)
                if root.value.right_child is not None:
                    custom_queue.enqueue(root_node.value.data)
                return "Not Found"

    def insert(root_node, new_node):
        if not root_node:
            root_node = new_node
        else:
            ifcustom_queue = queue.queue()
            custom_queue.enqueue(root_node)
            while not (custom_queue.isempty()):
                root = custom_queue.dequeue()
                if root_node.left_child is not None:
                    custom_queue.enqueue(root_node.left_child)
                else:
                    root_node.left_child = new_node
                    return ('Successfully inserted')
                if root_node.right_child is not None:
                    custom_queue.enqueue(root_node.right_child)
                else:
                    root_node.left_child = new_node
                    return ('Successfully inserted')
    #Deepest node is replaced with specified node to be deleted
    def get_deepest_node(root_node):
        if not root_node:
            return
        else:
            custom_queue = queue.queue()
            customQueue.enqueue(root_node)
            while not(customQueue.isempty):
                root = custom_queue.dequeue()
                if root.value.left_child is not None:
                    custom_queue.enqueue(root_node.value.data)
                if root.value.right_child is not None:
                    custom_queue.enqueue(root_node.value.data)
            deepest_node = root.value
            return deepest_node

    def delete_deepest_node(root_node, deepest_node):
        if not root_node:
            return
        else:
            custom_queue = queue.queue()
            custom_queue.enqueue(root_node)
            while not (custom_queue.isempty()):
                root = custom_queue.dequeue()
                if root.value is deepest_node:
                    root.value = None
                    return
                if root.value.right_child:
                    if root.value.right_child is deepest_node:
                        root.value.right_child = None
                        return
                    else:
                        custom_queue.enqueue(root.value.right_child)
                if root.value.left_child:
                    if root.value.left_child is deepest_node:
                        root.value.left_child = None
                        return
                    else:
                        custom_queue.enqueue(root.value.left_child)
    def delete_node(root_node,node):
        if not root_node:
            return("The BT does not exist")

        else:
            custom_queue = queue.queue()
            custom_queue.enqueue(root_node)
            while not (custom_queue.isempty()):
                root = custom_queue.dequeue()
                if root.value.data == node:
                    deepest_node = get_deepest_node(root_node)
                    root.value.data = deepest_node
                    delete_deepest_node(root_node,deepest_node)
                    return("The node has been deleted")
                if (root.value.left_child is not None):
                    custom_queue.enqueue(root.value.left_child)
                if (root.value.right_child is not None):
                    custom_queue.enqueue(root.value.right_child)
                return ('Failed to Delete')

    def delete(root_node):
        root_node = None
        root_node.left_child = None
        root_node.right_child = None
