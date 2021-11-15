def factor(n):
    div=2
    while(n>1):
        if(n%div==0):
            print(div,end=' ')
            n=n//div
        else:
            div=div+1

factor(120)            