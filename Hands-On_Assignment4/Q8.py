import math
x=float(input("Enter x: "))
sum=1
term=1
i=0
while(math.fabs(term)>0.000001):
    i=i+1
    term=(x/i)*term
    sum=+term
print("Taylor series sum = ",sum)
print(math.exp(x))