# Дано три числа. Упорядочите их в порядке неубывания. Программа должна считывать три
# числа a, b, c, затем программа должна менять их значения так, чтобы стали выполнены
# условия a <= b <= c, затем программа выводит тройку a, b, c.
# Дополнительные ограничения: нельзя использовать дополнительные переменные.

a = int(input("Please enter first number:\n"))
b = int(input("Please enter second number:\n"))
c = int(input("Please enter third number:\n"))

if a > b:
    a, b = b, a

if b > c:
    b, c = c, b

if a > b:
    a, b = b, a

print("The answer is:", a, b, c,".")