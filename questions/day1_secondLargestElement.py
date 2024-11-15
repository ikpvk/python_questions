array = [12, 34, 45, 32, 54]

max1=-1
max2=-1

for i in array:
    if(max1 < i) :        
        max2 = max1
        max1 = i

    elif max2 < i and i < max1 :
        max2 = i

print(max2)