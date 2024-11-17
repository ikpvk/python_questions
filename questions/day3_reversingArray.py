arr=[1,2,3,4,5,6]
print("scenario 1")
print("before ")
print(arr)
arrLen = len(arr)
if arrLen>1:
    for i in range (0,int(arrLen/2)):
        arr[i],arr[arrLen-i-1]=arr[arrLen-i-1],arr[i]

print("after")
print(arr)

print("scenario 2")
arr=[1,2,3]
print("before ")
print(arr)
arrLen = len(arr)
if arrLen>1:
    for i in range (0,int(arrLen/2)):
        arr[i],arr[arrLen-i-1]=arr[arrLen-i-1],arr[i]

    print("after")
    print(arr)