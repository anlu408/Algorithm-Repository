'''
#Search algorithm with logarithmic time complexity.
Splits an array in half, and searches for the correct value.
Low and high as first and last element in array, and mid used to find center
Guess used to store array element to compare with item.
'''
def binary_search(list,item):

    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low+high) / 2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1
        return None

'''
Function takes in an array (in our case list), and a value to search for
in the array.

Low- The start of the array (element 0)
High- The end of the array (last element in the array)
Guess- The midpoint of the array
'''
