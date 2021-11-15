def checkPrime(n):
    c=0
    for i in range(2,(n//2)+1):
        if(n%i==0):
            return False
    return True

n=int(input('Enter a number: '))
if(n>1):
    print(checkPrime(n))
else:
    print("False")

            