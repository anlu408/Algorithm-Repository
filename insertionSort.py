#sample array
array = [11, 34, 14, 23, 44, 55]
'''
The while loop swaps the values of current key and next element if the key is
smaller than current element it is being compared to
'''
#insertion sort for loop
for i in range (1, len (array)):
#define key to first element of array
    key = array[i]
#j is used to set array back to first element
    j = i-1
#while loop to compare. Use j >= 0 to compare to previous elements
    while j >= 0 and key < array[j]:
        array[j+1] = array[j]
        #Swaps the value of the the elements in the array
        j -= 1
    array[j+1] = key

print(array)

'''
Analysis
The Algorithm starts by setting i = 1, j = 0 and key = 34. Key is first
compared to array[j] which is 11. Since 34 > 11, the while loop is not executed.
Array state: [11, 34, 14, 23, 44, 55]

The next case to follow sets i = 2 and j = 1 and key is still 34. Key is then
compared to array[1] which is still 34. While loop does not execute.
Array state: [11, 34, 14, 23, 44, 55]

Next case: i = 3 j = 2 and key still 34. Key is then compared to array[2] which
is 14. The while loop condition is now fulfilled as key is greater than 14.
array[3] is set to 34 while array[2] is set to 14. J's value is then dropped to
1.
Array state: [11, 14, 34, 23, 44, 55]

Next case: i = 4, j = 3 and key is set to 23. 23 is compared to array[3] which
is 34. Since 23<34, the while loop's condition is fulfilled. array[3] and
array[4] will switch values setting array[3] to 23 and array[4] to 34.

Array state: [11, 14, 23, 34, 44, 55]

The while loop should continue to loop through the rest of the elements in the
array without error.
'''
