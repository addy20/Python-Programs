def anagram(s1,s2):
    if (len(s1)!=len(s2)):
        return False
    else:
        sorted(s1)
        sorted(s2)
        if(s1==s2):
            return True
        return False        
s1='book'
s2='koob'  
print(anagram(s1,s2))  
