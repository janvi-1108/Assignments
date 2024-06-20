num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
while(True):
    x=input("Enter the operation you wish to perform: ")
    if x=='+':
        print(num1+num2)
    elif x=='-':
        print(num1-num2)
    elif x=='*':
        print(num1*num2)
    elif x=='/':
        print(num1/num2)
    elif x=='//':
        print(num1//num2)
    elif x=='%':
        print(num1%num2)