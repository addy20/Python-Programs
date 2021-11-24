import pdb
pdb.set_trace()

def summation(n):
    total=0
    for count in range(1,n+1):
        total=total+count
    return total

n=int(input("Enter number of terms: "))
total=summation(n)
print('Sum of first',n,'positive integers:',total)