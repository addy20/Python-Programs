def symmetric(str):
    return str[0:len(str)//2]==str[len(str)//2:len(str)]
str=input('Enter a string:\n')
if(len(str)%2!=0):
    print('False')
else:
    print(symmetric(str))
        