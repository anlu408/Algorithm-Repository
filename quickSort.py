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

array = [4,8, 2,1,5,7,6,3]
s = 0
e = len(array) - 1
print (quickSort(array, s, e))
