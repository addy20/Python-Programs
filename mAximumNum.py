# import pdb
# pdb.set_trace()

def max(n1,n2,n3):
    maxNumber=0
    if(n1>n2):
        if(n1>n3):
            maxNumber=n1  
        else:
            maxNumber=n3    
    elif(n2>n3):
        maxNumber=n2
    else:
        maxNumber=n3
    return maxNumber
def main():
    n1=int(input("Enter n1: "))
    n2=int(input("Enter n2: "))
    n3=int(input("Enter n3: "))
    print('Maximum Number is: ',max(n1,n2,n3))

if(__name__=='__main__'):
    main()