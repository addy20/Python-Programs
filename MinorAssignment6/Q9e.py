def delete(str,n):
    ans=''
    for i in range(len(str)):
        if(i==n):
            continue
        ans=ans+str[i]
    return ans    
str=input('Enter a string:\n')
n=3
print(delete(str,n))        

