
a = [11,21,33]
b = [12,52,64]
c = a + b
c=[11,21,33,44,52,12,64]

#C at this point: [11, 21, 33, 12, 52, 64]
#Expected output: [11, 12, 21, 33, 52, 64]

middle = int(len(c) / 2)

left = c[:middle]
right = c[middle:]

d = int(len(left))
e = int(len(right))

i = j = k = 0

while((i < d) and (j < e)):
    if(left[i] < right[j]):
        c[k] = left[i]
        i += 1
    else:
        c[k] = right[j]
        j += 1
    k += 1

#The portion of the code below is supposed to check the remaining elements but I
#can't quite figure out how to get this to work yet.

while (i<d):
    c[k] = left[i]
    i += 1
    k += 1
while (j < e):
    c[k] = right[j]
    j  += 1
    k += 1

print(c)

'''
Analysis:
Takes an array, splits the array into two halves left and right.First element
in left is compared to first element in right. If left element is larger,
first element in the sorted array while be set equal to first element in left
and if not, set to first element in right.
'''
