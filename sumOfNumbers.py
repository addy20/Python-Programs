from itertools import count
total=0
num=input("Enter a number: ")

for i in count(0):
    if(num==""):
        break
    total+=int(num)
    num=input("Enter a number: ")

print("Sum of all input numbers is = ",total)