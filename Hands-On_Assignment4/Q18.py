def sequenceGen(n):
    c=1
    while(n>0):
        n=n-1
        print(c,end=" ")
        c=2*c

n=int(input("Enter the value of n to generate sequence: "))
sequenceGen(n)
