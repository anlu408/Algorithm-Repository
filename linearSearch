#Quick Linear Search

array = [10, 15, 20,  25, 30]
key = 31

def linearSearch(array, key):
#Note that here you must use len(array) as it stops at the value just before len(array)
    for i in range (0, len(array)):
        if (key == array[i]):
            return i
        else:
            i += 1

        if (i == len(array)):
            return -1

print (linearSearch(array, key))

'''
Linear Search algorithm.

O(N) time complexity as it loops through each element of an array once.

You have an array (list of values to search through) and a key (value to search for).
If the key is equal to the value of the array that you compare to the index number
of the array is returned.

If the value is not in the array, None is returned

Results:
10 returns 0
15 returns 1
20 returns 2
25 returns 3
30 returns 4
31 returns -1
'''
