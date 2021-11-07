def rootsOfQuadEq(a,b,c):
    D=(b*b)-(4*a*c)
    if(D>0):
        print("The equation has two real roots.")
    elif(D==0):
        print("The equation has one root.")
    else:
        print("The equation has no real roots.")        


a=float(input("Enter value of a:\n"))
b=float(input("Enter value of b:\n"))
c=float(input("Enter value of c:\n"))

rootsOfQuadEq(a,b,c)