def selectionSort(array):

    smallest = array[0]
    smallestIndex = 0
    temp = 0

    for i in range (0, len(array)):
        smallest = array[i]
        for j in range (i, len(array)):
            if(smallest > array[j]):
                smallest = array[j]
                smallestIndex = j

        array[smallestIndex], array[i] = array[i], array[smallestIndex]

array = [5,3,4,1,2]
selectionSort(array)
print(array)

'''
Selection Sort:
Finds the smallest element and swaps it with the correction position
in the array.

With the first loop iteration i = 0 and j loops from 0 to 4. Smallest is
initially 5 because of the array [5,3,4,1,2] smallest is compared to each value
in the array and if compared to a smaller element in the array, smallest is set
to that value. We also record the index of the array to swap the two values.

After the first swap (swapping the smallest number found from elements 0 to 4
with element 0 indicating the smallest number in the array.

What follows is i is increased by 1 and the loop will now sort through elements
1-4 because we know that 0 is already the smallest element in the array.
This will continue and find the smallest elements in 1-4, 2-4, 3-4 and
eventually just 4.
'''
