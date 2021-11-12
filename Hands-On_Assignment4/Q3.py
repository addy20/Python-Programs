n=int(input("\nEnter value of n:"))
sum=0
m=1

assert n>=1
for i in range(1,2*n,2):
    sum+=(i*m)
    m=m*(-1)

print("The sum of the first n terms of the series S=1-3+5-7+9- ……… is %d\n"%(sum))    


