def squareRoot(n):
    x=n
    while(True):
        root=0.5*(x+(n/x))
        print(x,"   ",root)
        if(abs(root-x)<0.000001):
            break
        x=root
    print("The root is: ",root)

n=int(input("Enter the value of n: "))
squareRoot(n)
