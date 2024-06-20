lst=lst=[1,2,1,5,98,65,74,25,77,1,65,1]
min=lst[0]
max=lst[0]

for i in range(len(lst)):
    if lst[i]>max:
        max=lst[i]
    elif lst[i]<min:
        min=lst[i]

print("The maximum value is ",max)
print("The minimum value is ",min)