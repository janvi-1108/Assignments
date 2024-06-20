s1=input("Enter a string: ")
s2=str()
for i in range(len(s1)):
    if s1[i].isalnum() or s1[i]==' ':
        s2=s2+s1[i]
print(s2)