def convertToUppercase(str):
    list=str.split()
    ans=''
    for i in range (0,len(list)):
        mid_value=capitalize(list[i])
        ans=ans+mid_value+' '
    return ans    
def capitalize(str):
    fChar=str[0]
    restChar=''
    if(97<=ord(fChar)<=122):
        fChar=chr(ord(str[0])-32)
    for i in range (1,len(str)):
        if(97<=ord(str[i])<=122):
            restChar=restChar+str[i]
        else:
            restChar=restChar+chr(ord(str[i])+32)    
    return fChar+restChar
 
str=input('Enter a sentence: ')
print(convertToUppercase(str))   
        

