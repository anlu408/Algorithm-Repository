def findSmallest(arr):

    smallest = arr[0]
    smallest_index = 0

    for i in range (1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = 1
            return smallest_index

'''
Analysis

Smallest defined as the first element in the array and we created another
variable smallest index to compare the first element in the array to the next
element in the array. The loop will keep going through until all elements in
the array have been sorted.

Time Complexity: O(n^2)
'''
