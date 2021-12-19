def count(str):
    c,d=0,0
    for i in str:
        if(ord(i)>=97 and ord(i)<=122 or ord(i)>=65 and ord(i)<=90):
            c=1
        elif(ord(i)>=48 and ord(i)<=57):
            d=1  
    return True if(c==1 and d==1) else False 
str=input('Enter a string: ')
print(count(str))    
            
            