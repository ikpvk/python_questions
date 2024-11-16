array = [1,2,0,4,3,0,5,0]

nonZeroPointer = 0

for i in range(len(array)):
    if array[i] != 0:
        array[nonZeroPointer] = array[i]
        nonZeroPointer+=1

for i in range(nonZeroPointer,len(array)):
    array[i] = 0

print(array)