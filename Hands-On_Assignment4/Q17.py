import sys
def checkPrime(n):
    if(n>1):
        for i in range(2,(n//2)+1):
            if(n%i==0):
                return False
        return True
    else:
       return False
    

n=int(sys.argv[1])
for i in range(2,n+1):
    if(checkPrime(i)):
        print(i,end=' ')



            