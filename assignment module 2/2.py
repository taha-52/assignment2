fact=1
num=int(input("enter a num: "))
if num<0:
    print("fact is not define")
else:
      for i in range(1,num+1):
           fact*=i
print(fact)
