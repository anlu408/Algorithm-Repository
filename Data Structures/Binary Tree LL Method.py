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
