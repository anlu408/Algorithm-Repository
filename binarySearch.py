#Defines an array
list = []
#Defines low and high as low/high values of array, mid to find center
low = 0
high = len(list)-1
mid = (low+high)/2
#guess is the starting point of the search
guess = list[mid]

#Splits an array in half, and searches for the correct value.

'''
Function takes in an array (in our case list), and a value to search for
in the array.

Low- The start of the array (element 0)
High- The end of the array (last element in the array)
Guess- The midpoint of the array
'''

def binary_search(list,item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low+high)
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1
        return None
