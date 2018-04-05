# Даны три числа a, b, c. Определите, существует ли треугольник с такими сторонами. Если
# треугольник существует, выведите строку YES, иначе выведите строку NO.

a = float(input("Please enter first side of the triangle:\n"))
b = float(input("Please enter second side of the triangle:\n"))
c = float(input("Please enter third side of the triangle:\n"))

if a + b > c and a + c > b and b + c > a:
    print('YES. This triangle exists.')
else:
    print("NO. This triangle doesn't exist.")