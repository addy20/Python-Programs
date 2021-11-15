def Fibonacci(n):
   a = 0
   b = 1
   print("Fibonacci Series: ", end = " ")
   while (n-2>0):
      n=n-2
      print(a,b, end = " ")
      a=a+b
      b=a+b

n = int(input("Enter the value of 'n': "))
Fibonacci(n)

   