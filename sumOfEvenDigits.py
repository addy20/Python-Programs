def sumOfEvenDigits(n):
    sum=0
    while(n>0):
        d=n%10
        if(d%2==0):
         sum=sum+(d)
        n=n//10 
    return sum
   
   
n=int(input("Enter a Number: "))
print("Sum of even digits= ",sumOfEvenDigits(n))