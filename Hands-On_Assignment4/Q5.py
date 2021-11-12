import math
def power(x,n):
    return math.pow(x,n) 

def fact(n):
    f=1
    for i in range(2,n+1):
        f=f*i
    return f

x=int(input("Enter the value of x: "))
n=int(input("Enter the value of n: "))

ans=power(x,n)/fact(n)
print("Answer is:",ans)
