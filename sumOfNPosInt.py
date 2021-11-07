def sumN(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total

def sumOfEvenN(n):
    total=0
    for i in range(0,n+1,2):
        total+=i
    return total 

def sumOfoddN(n):
    total=0
    for i in range(1,n+1,2):
        total+=i
    return total


n=int(input("Enter number of terms: "))
total=sumN(n)
evenSum=sumOfEvenN(n)
oddSum=sumOfoddN(n)
print("Sum of first",n,"positive integers: ",total)
print("Sum of first",n,"even positive integers: ",evenSum)   
print("Sum of first",n,"odd positive integers: ",oddSum)    
