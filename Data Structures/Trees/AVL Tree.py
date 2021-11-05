'''
AVL Tree- A self balancing BST where differences between heights of L/R subtrees cannot be more than one for all nodes

Any time the height of subtrees differ by more than 1, the AVL tree is rebalanced in a process called rotation
'''

class avl_node:
    def __init__(self, value):
        self.data = value
        self.left_child = None
        self.right_child = None
        self.height = 1

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

    def search_avl(root_node, value):
        if root_node.data == value:
            return ('The value is found')
        elif value < root_node.data:
            if root_node.left_child.data == value:
                return("The value is found")
            else:
                search_avl(root_node.left_child, value)
        elif value > root_node.data:
            if root_node.right_child.data == value:
                return ("The value is found")
            else:
                search_avl(root_node.right_child, value)

    def get_height(root_node):
        if not root_node:
            return 0
        else:
            return root_node.height

    def right_rotation(disbalanced_node):
        new_root = disbalanced_node.left_child
        disbalanced_node.left_child = disbalanced_node.left_child.right_child
        new_root.right_child = disbalanced_node
        disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
        new.height = 1 + max(get_height(new.left_child), get_height(new.right_child))
        return new_root

    def left_rotation(disbalanced_node):
        new_root = disbalanced_node.right_child
        disbalanced_node.right_child = disbalanced_node.left_child.right_child
        new_root.left_child = disbalanced_node
        disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
        new.height = 1 + max(get_height(new.left_child), get_height(new.right_child))
        return new_root

    def get_balance(root_node):
        if not root_node:
            return 0
        return(get_height(root_node.left_child) - get_height(root_node.right_child))

    def insert_node(root_node, value):
        if not root_node:
            return avl_node(value)
        elif value < root_node.data:
            root_node.left_child = insert_node(root_node.left_child, value)
        else:
            root_node.right_child = insert_node(root_node.right_child, value)

        root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
        balance = get_balance(root_node)
        #Left-Left Condition
        if balance > 1 and value < root_node.left_child.data:
            return right_rotation(root_node)
        #Left-Right condition
        if balance > 1 and value > root_node.left_child.data:
            root_node.left_child = left_rotation(root_node.left_child)
            return right_rotation(root_node)
        #Right-Right condition
        if balance < -1 and value > root_node.right_child.data:
            return left_rotation(root_node)
        #Right-Left Condition
        if balance < -1 and value < root_node.right_child.data:
            root_node.right_child = right_rotation(root_node.right_child)
            return left_rotation(root_node)

        def get_minimum(root_node):
            if root_node is None or root_node.left_child is None:
                return root_node
            return get_minimum(root_node.left_child)

        def delete_node(root_node,value):
            if not root_node:
                return root_node
            elif value < root_node.data:
                root_node.left_child = delete_node(root_node.left_child, value)
            elif value > root_node.data:
                root_node.right_child = delete_node(root_node.right_child, value)
            else:
                if root_node.left_child is None:
                    temp = root_node.right_child
                    root_node = None
                    return temp
                if root_node.right_child is None:
                    temp = root_node.left_child
                    root_node = None
                    return temp

                temp = get_minimum(root_node.right_child)
                root_node.data = temp.data
                root_node.right_child = delete_node(root_node.right_child, temp.data)

            balance = get_balance(root_node)
            if balance > 1 and get_balance(root_node.left_child) >= 0:
                return right_rotation(root_node)
            if balance < -1 and get_balance(root_node.right_child) <= 0:
                return left_rotation(root_node)
            if balance > 1 and get_balance(root_node.left_child) < 0:
                root_node.left_child = left_rotation(root_node.left_child)
                return right_rotation(root_node)
            if balance < -1 and get_balance(root_node.right_child) > 0:
                root_node.right_child = right_rotation(root_node.right_child)
                return right_rotation(root_node)

        def delete_avltree(root_node):
            root_node.data = None
            root_node.left_child.data = None
            root_node.right_child.data = None
            return ("The AVL tree has been deleted")
