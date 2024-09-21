"""
a=int(input("enter num "))
b=int(input("enter second num "))
temp=a
a=b
b=temp
print("after swapping")
print(a)
print(b)
"""
a=int(input("enter num "))
b=int(input("enter second num "))
a=a+b
b=a-b
a=a-b
print("after swapping")
print(a)
print(b)