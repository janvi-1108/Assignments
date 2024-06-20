num=int(input("Enter a number: "))
fact=1
if num==0 or num==1:
    print("The factorial is 1")
elif num>0:
    for i in range(1,num+1):
        fact=fact*i
    print("The factorial is ",fact)
else:
    print("Invalid Input")