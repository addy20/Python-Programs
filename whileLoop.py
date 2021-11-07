def usingForLoop(n):
    s=0
    for i in range(n):
        r=n%10
        n=n//10
        s=s+r
        if(n==0):
            break
    return s   
  
  
n=input("Enter a number: ")
# s=0
# while(n>0):
#     r=n%10
#     n=n//10
#     s=s+r

# print(s)
print(usingForLoop(n))

