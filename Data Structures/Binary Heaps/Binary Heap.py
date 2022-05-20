'''
Binary heaps- Useful for finding min/max in logN time and insertion also
does not take more than logN time.

Min Heap- Value of each node less than or equal to value of both children
Max Heap- Value of each node more than or equal to value of both children

Common Operations
Creation
Peek top
Extract Min/Max
Find size
Insert Value
Delete entire heap
'''

class heap:
    def __init__(self, size):
        self.custom_list = (size + 1) * None
        self.heap_size = 0
        self.max_size = size + 1

    def peek(root_node):
        if not root_node:
            return
        else:
            return root_node.custom_list[1]

    def size_of_heap(root_node):
        if not root_node:
            return
        else:
            return root_node.heap_size

    def levelorder_traversal(root_node):
        if not root_node:
            return
        else:
            for i in range (1, root_node.heap_size + 1):
                print(root_node.custom_list[i])

    def heapify_insert(root_node, index, type):
        parent_index = int(index / 2)
        if index <= 1:
            return
        if type == "Min":
            if root_node.custom_list[index] < root_node.custom_list[parent_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[parent_index]
                root_node.custom_list[parent_index] = temp
            heapify_insert(root_node, parent_index, type)

        elif type == "Max":
            if root_node.custom_list[index] > root_node.custom_list[parent_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[parent_index]
                root_node.custom_list[parent_index] = temp
            heapify_insert(root_node, parent_index, type)


    def insert_node(root_node, value, type):
        if root_node.heap_size + 1 == root_node.max_size:
            return ("The binary heap is full")
        root_node.custom_list[root_node.heap_size + 1] == value
        heapify_insert(root_node, root_node.heap_size, type)
        return("The vaue has been inserted")

    def heapify_extract(root_node, index, type):
        left_index = index * 2
        right_index = index * 2 + 1
        swap_child = 0

        if root_node.heap_size < left_index:
            return
        elif root_node.heap_size = left_index:
            if type == "Min":
                if root_node.custom_list[index] > root_node.custom_list[left_index]:
                    temp = root_node.custom_list[index]
                    root_node.custom_list[index] = root_node.custom_list[left_index]
                    root_node.custom_list[left_index] = temp
                    return
                else:
                    if root_node.custom_list[index] < root_node.custom_list[left_index]:
                        temp = root_node.custom_list[index]
                        root_node.custom_list[index] = root_node.custom_list[left_index]
                        root_node.custom_list[left_index] = temp
                    return
        else:
            if type == "Min":
                if root_node.custom_list[left_index] < root_node.custom_list[right_index]:
                    swap_child = left_index
                else:
                    swap_child = right_index
                if root_node.custom_list[index] > root_node.custom_list[swap_child]:
                    temp = root_node.custom_list[index]
                    root_node.custom_list[index] = root_node.custom_list[swap_child]
                    root_node.custom_list[swap_child] = temp
            else:
                if root_node.custom_list[left_index] > root_node.custom_list[right_index]:
                    swap_child = left_index
                else:
                    swap_child = right_index
                if root_node.custom_list[index] < root_node.custom_list[swap_child]:
                    temp = root_node.custom_list[index]
                    root_node.custom_list[index] = root_node.custom_list[swap_child]
                    root_node.custom_list[swap_child] = temp
                heapify_extract(root_node, swap_child, type)

    def extract_node(root_node, type):
        if root_node.heap_size == 0:
            return
        else:
            extracted = root_node.custom_list[1]
            root_node.custom_list[1] = root_nopde.custom_list[root_node.heap_size] = None
            root_node.heap_size -= 1
            heapify_extract(root_node,1,type)
            return('Extracted')
    def delete_heap(root_node):
        root_node.custom_list = None
