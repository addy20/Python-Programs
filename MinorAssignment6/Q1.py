def starReplace(str):
    st=str[0]
    for i in range (1,len(str)):
        if(str[i-1]!=str[i]):
            st=st+str[i]
        else:
            st=st+'*'
    return st
str=input("Enter a String: ")
print(starReplace(str))