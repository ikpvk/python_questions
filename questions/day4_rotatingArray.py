array: list[int] = [1,2,3,4,5]
d:int = 12
arrLen = len(array)

d = d % arrLen

print(d," ",arrLen," ",array)

# Reverse first d elements
for i in range(0,int(d/2)):
    revIndex = d-i-1
    array[i],array[revIndex] = array[revIndex],array[i]
print(array)

# Reverse next len - d elements
for i in range(0, int((arrLen-d)/2)):
    startIndex = d+i
    revIndex = arrLen-i-1
    array[startIndex],array[revIndex] = array[revIndex],array[startIndex]
print(array)

# Reverse the whole array
for i in range(0,int(arrLen/2)):
    array[i],array[arrLen-i-1] = array[arrLen-i-1],array[i]
print(array)