def quadrant(x, y):
    if(x>0 and y>0):
        print (x,y,"is in First quadrant")
    elif(x<0 and y>0):
        print (x,y,"is in Second quadrant")  
    elif (x<0 and y<0):
        print (x,y,"is in Third quadrant")
    elif(x>0 and y<0):
        print (x,y,"is in Fourth quadrant")
    elif(x==0 and y>0):
        print (x,y,"is at positive y axis")
    elif (x==0 and y<0):
        print (x,y,"is at negative y axis")
    elif (y==0 and x<0):
        print (x,y,"is at negative x axis")
    elif (y==0 and x>0):
        print (x,y,"is at positive x axis")
    else:
        print (x,y,"is at origin")


x = float(input("Enter x: \n"))
y = float(input("Enter y: \n"))
quadrant(x, y)