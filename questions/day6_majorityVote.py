arr = [2 ,1,5,5,5, 5, 5, 5, 5, 6, 6, 6, 6, 6]

arrLen = len(arr)
        
# if arrLen == 1:
#     return arr
    
majorityCount = int(arrLen/3)

arr.sort()

resultArr = []

counter = 1
for i in range(1,arrLen):
    if arr[i-1] == arr [i]:
        counter=counter+1
    else:
        if counter>majorityCount:
            resultArr.append(arr[i-1])
        counter=1

if counter>majorityCount:
    resultArr.append(arr[arrLen-1])

print(resultArr)