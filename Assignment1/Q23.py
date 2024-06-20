ch=input("do you wish to enter temperature in celsius(c) or fahrenheit(f): ")
if ch=='c':
    c=float(input("Enter temperature in Celsius: "))
    x=(c*1.8)+32
    print("Temperature is Fahrenheit is ",x)
elif ch=='f':
    f =float(input("Enter temperature in Fahrenheit: "))
    y=(f-32)/1.8
    print("Temperature is Celsius is ",y)
else:
    print("Invalid input")