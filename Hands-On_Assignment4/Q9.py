def Fibonacci(n):
   a,b= 0,1
   sum = 0
   print("Fibonacci Series: ", end = " ")
   while (n>0):
      n=n-1
      print(sum, end = " ")
      a = b
      b = sum
      sum = a + b


n = int(input("Enter the value of 'n': "))
Fibonacci(n)

   