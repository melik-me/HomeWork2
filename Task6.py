# Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести
# одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).

a = int(input("Please enter first number:\n"))
b = int(input("Please enter second number:\n"))
c = int(input("Please enter third number:\n"))

if a == b == c:
    print("The answer is 3.")
elif a == b or b == c or a == c:
    print("The answer is 2.")
else:
    print("The answer is 0.")