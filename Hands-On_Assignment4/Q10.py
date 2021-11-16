def Fibonacci(n):
   a = 0
   b = 1
   print("Fibonacci Series: ", end = " ")
   count=2
   while(n>count):
      print(a,b, end = " ")
      a=a+b
      b=a+b
      count=count+2
   if(count-n==0):
       print(a,b,end=' ')
   else:
       print(a)          

n = int(input("Enter the value of 'n': "))
Fibonacci(n)

   