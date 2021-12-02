num=int(input("Enter n : "))
sum=0
digit=num//1000
sum+=(1-digit%2)*digit
digit1=(num-(digit*1000))//100
sum+=(1-digit1%2)*digit1
digit2=(num-(digit*1000)-(digit1*100))//10
sum+=(1-digit2%2)*digit2
digit3=(num-(digit*1000)-(digit1*100)-(digit2*10))
sum+=(1-digit3%2)*digit3
print(sum)

