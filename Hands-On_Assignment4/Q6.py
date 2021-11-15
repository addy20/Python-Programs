import math
x=float(input("Enter the value of x: "))
r=math.radians(x)
tsin=r
term=r
i=1


while(math.fabs(term)>0.000001):
    i=i+2
    term=(-term*r*r)/(i*(i-1));
    tsin=tsin+term


print('sin(',x,')= ',tsin)



