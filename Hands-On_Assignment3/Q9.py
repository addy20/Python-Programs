import math
print("Enter a point with two coprdinates:")
x=float(input("x: "))
y=float(input("y: "))

D=math.sqrt((x*x)+(y*y))
if(D<10):
    print("Point (%.1f,%.1f) is in the circle." %(x,y))
elif(D==10):
    print("Point (%.1f,%.1f) is on the circle." %(x,y)) 
else:
    print("Point (%.1f,%.1f) is not in the circle." %(x,y))
