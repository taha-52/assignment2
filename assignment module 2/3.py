start=int(input("enter start point : "))
end=int(input("enter end point : "))
if start>end:
    print("start cannot be greater then end")
else:
    a=0
    b=1
    fib_series=[]    
while a<=end:
    if a>=start:
        fib_series.append(a)
        a,b=b,a+b
        print("fibonaci series is", fib_series)