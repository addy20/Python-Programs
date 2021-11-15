import math
x=float(input("Enter the value of x: "))
r=math.radians(x)
tcos=1
term=1
i=0


while(math.fabs(term)>0.000001):
    i=i+2
    term=(-term*r*r)/(i*(i-1));
    tcos=tcos+term


print('cos(',x,')= ',tcos)



