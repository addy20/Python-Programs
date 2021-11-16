def factChecker(n):
    c=0
    for i in range(2,(n//2)+1):
        if(fact(i)==n):
            print("Exist!",i)
            c=+1
            return
    if(c==0):
        print("Not Exist!!")
            

def fact(n):
    f=1
    while(n>=2):
        f=f*n
        n=n-1
    return f    

n=int(input("Enter n:"))
factChecker(n)