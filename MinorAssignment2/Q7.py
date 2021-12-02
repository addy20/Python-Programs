import math
def areaTriangle(s1,s2,s3):
    assert (s1+s2>s3) or (s1+s3>s2) or (s2+s3>s1)
    s = (s1 + s2 + s3)/2
    area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    return area

s1=int(input("Enter s1: "))
s2=int(input("Enter s2: "))
s3=int(input("Enter s3; "))
print("Area of Triangle =",areaTriangle(s1,s2,s3))