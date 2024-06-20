s1=input("Enter first string: ")
s2=input("Enter second string: ")

s1=sorted(s1.lower())
s2=sorted(s2.lower())

if s1==s2:
    print("Yes, the strings are anagrams")
else:
    print("No, the strings are not anagrams")


