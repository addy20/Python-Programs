def reverse(n):
    sum=0
    while(n>0):
        rem=n%10
        sum=sum*10+rem
        n=n//10
    return sum

n=int(input("Enter the number: "))
print("Reverse = ",reverse(n))
