array = [26, 50, 32, 19, 7]

def bubbleSort(array):
    for i in reversed((range(len(array)))):
        for j in reversed(range(len(array) - 1)):
            print(array)
            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]


bubbleSort(array)
print(array)

'''
The algorithm starts from 7.
7<19-> switch 7 and 19

resulting array:
[26,50,32,7,19]

then the next number is compared
following arrays:
[26,50,7,32,19]
[26,7,50,32,19]
[7,26,50,32,19]

The inner loop is complete and now the outer loop runs.
19<32 -> swap
resulting array: [7,26,50,19,32]
now the inner loop will run until completion
[7,26,19,50,32]
[7,19,26,50,32]
7<19 so no swap occurs. Inner loop completes again

outer loop runs
32<50
resulting array: [7,19,26,32,50]
32<26 and 19 and 7 so no more swaps occur.
'''
