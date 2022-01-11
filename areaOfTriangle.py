def areaCalc(a, b, c):
    s = (a + b + c) / 2
    assert (a + b > c and b + c > a and c + a > b)
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print('The area of the triangle is %.2f' % area)


a = float(input('Enter length of 1st side:\n'))
b = float(input('Enter length of 2nd side:\n'))
c = float(input('Enter length of 3rd side:\n'))

areaCalc(a, b, c)



