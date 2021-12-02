def Fibonacci(d,e):
    n=max(d,e)
    a,b=0,1
    for i in range (n+1):
        c=a+b
        a=b
        b=c
        if((d==a and e==b) or (d==b and e==a)):
            return True
    return False        

d=int(input("Enter d: "))
e=int(input("Enter e: "))

if((d==0 and e==1) or (d==1 and d==0)):
    print(True)
else:
    if(Fibonacci(d,e)):
        print(True)
    else:
        print(False)    


    