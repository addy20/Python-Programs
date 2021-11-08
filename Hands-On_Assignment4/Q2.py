c=0
for i in range (100,1001):
    if(i%5==0 and i%6==0):
        print(i,end=" ")
        c=c+1
    if(c==10):
        print()
        c=0