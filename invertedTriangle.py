def invertedTriangle(nRows):
    nSpaces=0
    type(nSpaces)
    nStars=2*nRows-1
    for i in range(1,nRows+1):
        print(' '*nSpaces+'*'*nStars)
        nStars-=2
        nSpaces+=1

def rightTriangle(nRows):
    for i in range(1,nRows+1):
        pass
        print('*'*i)


choice=int(input("Enter 1 for right Triangle.\n"+"Enter 2 for inverted Triangle.\n"))
assert choice==1 or choice==2
nRows=int(input("Enter number of Rows: "))

if(choice==1):
    rightTriangle(nRows)
else:
    invertedTriangle(nRows)    