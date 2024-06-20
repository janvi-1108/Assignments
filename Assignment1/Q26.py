s=input("Enter a string: ")
pre=input("Enter a prefix: ")
suf=input("Enter a suffix: ")

if pre in s or suf in s:
    print(f"The string starts/ends with {pre}/{suf}")