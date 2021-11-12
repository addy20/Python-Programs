def fact(n):
    f=1
    #for i in range(2,n+1):
    #     f=f*i
    
    # return f 
    while(n>=2):
        f=f*n
        n=n-1
    return f    

n=int(input("\nEnter the value of n: "))
print("Factorial of %d is %d.\n"%(n,fact(n)))
