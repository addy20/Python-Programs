def decimalToBinary(n):
    st=""
    while(n>0):
        rem=n%2
        st=str(rem)+st
        n=n//2
    return st  

n=int(input('Enter n: ')) 
print("Binary value: ",decimalToBinary(n))
