name=input("enter a string : ")
jas=input("enter second string: ")
col=len(name)//2
result=name[:col]+jas + name[col:]
print("total string is " , result )