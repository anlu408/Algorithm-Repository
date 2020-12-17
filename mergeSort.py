def mergeSort (array):
    middle = int(len(array) / 2)
    left = array[:middle]
    right = array[middle:]
    i = j = k = 0

    c=[]
    mergeSort(left)
    mergeSort(right)

    while (i < len(left)) and (j < len(right)):
        if(left[i] < right[j]):
            c[k] = left[i]
            i += 1
        else:
            c[k] = right[j]
            j += 1
        k += 1

    while (i < len(left)):
        c[k] = left [i]
        i += 1
        k += 1
    while(i < len(right)):
        c[k] = right[j]
        j += 1
        k += 1
