import math
x=float(input("Enter the value of x: "))
tsin=x
term=x
i=1


while(math.fabs(term)>0.000001):
    i=i+2
    term=-(x*x)/(i*(i-1))*term;
    tsin=tsin+term


print('sin(',x,')= ',tsin)



