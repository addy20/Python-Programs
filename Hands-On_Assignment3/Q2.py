ch=input("Please enter a character: ")
if(ch>='A' and ch<='Z'):
    print(ch," is an uppercase letter")
elif (ch>='a' and ch<='z'):
    print(ch," is a lowercase letter")
elif (ch>='0' and ch<='9'):
    print(ch," is a digit")    
else:
    print(ch," is a special symbol")

