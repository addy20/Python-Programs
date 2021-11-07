
mark=int(input('Enter mark : '))
if(mark<40):
    print('failed')
elif(mark>=40 and mark<75):
    print('Student passed and is good student')
elif(mark>=75 and mark<90):
    print('Student passed and is very good student')
else:
    print('Student passed and is extraordinary student')            