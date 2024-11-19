arr = [1,4,3,2]
print(arr)
pivot:int = -1
        
arrLen = len(arr)

if arrLen !=1:
    for i in range (arrLen-1,0,-1):
        if arr[i]>arr[i-1]:
            pivot=i-1
            break
        
    if pivot != -1:
        print("pivot ",pivot)
        for i in range (arrLen-1,pivot,-1):
            if arr[i] > arr[pivot]:
                arr[i],arr[pivot] = arr[pivot],arr[i]
                break
        
        left = pivot+1
        right = arrLen-1
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left = left + 1
            right = right -1
    else:
        arr.reverse()

print(arr)