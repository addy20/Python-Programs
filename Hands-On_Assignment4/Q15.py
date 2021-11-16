def gcdFinder(x,y):
    while(x!=y):
        if(x>y):
            x=x-y
        else:
            y=y-x    

    return x

x=int(input('Enter x: '))
y=int(input('Enter y: '))

print("GCD of (%d,%d) is "%(x,y),gcdFinder(x,y))
