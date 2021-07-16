def pivot(array, s, e):
    p = s #Stores pivot index
    k = p+1
    i = s+1 #general index

    while (i < len(array)): #loops through the rest of the array
        if(array[p] > array[i]): #If array[p] is greater, it is placed next to p.
            array[k],  array[i] = array[i], array[k]
            k += 1 #increase k to keep elements next to p.
            i += 1 #increase i to keep traversing the array
        else:
            i += 1 #if p is smaller, the array must still be traversed

    array[p] , array[k-1] = array[k-1], array[p] #Places p to the right of all of the values smaller than p in the array.
    return (k-1) #Used as the pivot index in the quick sort

def quickSort(array, s, e):
    if(s < e):
        pivot_index = pivot(array, s, e)
        quickSort (array, s, pivot_index - 1)
        quickSort (array, pivot_index + 1, e)
    return array

array = [4,8,2,1,5,7,6,3]
s = 0
e = len(array) - 1
print (quickSort(array, s, e))

'''
First I created a pivot function to find the correct index for the first element
of any given array.

p was used to store the index of the value being pivoted
k was used to move any value less than the pivot to the right of the pivot
and eventually swapping the last element that is smaller than the pivot in the
array with the pivot itself.

I.E. in the list [4,8,2,1,5,7,6,3] there are 3 elements smaller than 4.
(1,2 and 3). In the order that the array is set we end up with the array
[4,2,1,3,5,7,6,8] before the swap. k is set to the index for 3 and a swap
is performed between 4 and 3 as 3 is the last element that was swapped next to
the pivot. [3,2,1,4,5,7,6,8] is the result.

Since we had k increment each time the if statement was fulfilled to keep
traversing the array, we swapped p and the k-1 value as using k would only
swap the array after the last one that was swapped.

We return k-1 so that we can get the correct position of the first element of
any given array.

We then move to the actual quickSort function. We pass in the start and the end
of the array. start being the first element and end being the last element.

With the first recursive function call we have
[3,2,1,4,5,7,6,8]

With the first recursive function call we go from 0 to 2 as we know 4 is
already in the correct position (3). So [3,2,1] is what is passed into
quickSort. With the recursive function call quickSort is passed
0 to 1 and 1 to 2 to be sorted. This is because the first element should be
element 2 in the array.

With the right side we have [5,7,6,8] with a current pivot_index of 4.
This gives us an s value of 4 and and e value of 7. A recursive function call
occurs and splits elements 4 to 7 into 4 and 3 (does not exist) and
the right side which is 5 and 7. This is because from the pivot function call
we learned that 5 is already in the correct position. 5 to 7 which is
[7,6,8]. Pivot_index is set to 6 and quickSort then splits from 7 to 6 and
7 to 8. The same occurs until the entire array is sorted.
'''
