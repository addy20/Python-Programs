import re
def findWords(str):
    match=re.findall('[\w]+',str)
    return len(match)
str=input('Enter a Sentence:\n')
print(findWords(str))
