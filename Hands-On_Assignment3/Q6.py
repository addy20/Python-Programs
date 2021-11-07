def max(x,y,z):
    if(x>y and x>z):
        print("Rahul is elder.")
    elif(y>x and y>z):
        print("Ayush is elder.")
    else:
        print("Ajay is elder.") 


x=int(input("Enter age of Rahul:\n"))
y=int(input("Enter age of Ayush:\n"))
z=int(input("Enter age of Ajay:\n"))

max(x,y,z)





