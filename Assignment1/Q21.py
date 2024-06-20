ele=int(input("Enter the element you wish to find the occurence of: "))
lst=[1,2,1,5,98,65,74,25,77,1,65,1]
count=0
for i in range(len(lst)):
    if lst[i]==ele:
        count+=1
print("This element occurs ", count, " times")

