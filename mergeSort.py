
a = [11,21,33,44]
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

while (i<d):
    c[k] = left[i]
    i += 1
    k += 1
while (j < e):
    c[k] = right[j]
    j  += 1
    k += 1

print(c)


