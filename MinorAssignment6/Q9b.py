def reverseWords(str):
    return str[::-1]
def extractWords(str):
    list=str.split()
    ans=''
    for i in range(0,len(list)):
        ans=ans+reverseWords(list[i])+' '
    return ans       
str=input('Enter a String: ')
print(extractWords(str))