def count(str):
    str=str.lower()
    mstr=set(str)
    v=0
    c=0
    for i in mstr:
        if(i in 'aeiou'):
            v+=1
        else:
            c+=1
    return v,c
str=input('Enter a string: ')
print("Vowels,Consonants=",count(str))                

    
    