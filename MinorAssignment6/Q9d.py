def reverse(str):
    return str[::-1]
str=input('Enter a string:\n')
if(str==reverse(str)):
    print(True)
else:
    print(False)        