# Задание 2

# Вычислите длину гипотенузы в прямоугольном треугольнике со сторонами 179 и 971.

print('Cathetuses are 179 and 971. Hypotenuse is', ((179**2)+(971**2))**0.5,'.')

# Дано двузначное число. Найдите число десятков в нем.

q = 'y'

while q == 'y':
    n = int(input('Please enter a 2-digit number. I will try to count how many tens does it contain.\n'))
    if 9 < n <100:
        print('It contains', n // 10, 'tens.\n')
        q = input('Press "y" if you want to repeat this step.\n')
    else:
        print('Please enter valid 2-digit number.\n')
        q = 'y'

# Дано трехзначное число. Найдите сумму его цифр.

q = 'y'

while q == 'y':
    s = input("""Please enter a 3-digit number. I will try to calculate a sum of it's digits.\n""")
    n = int(s)
    if 99 < n < 1000:
        print('The answer is ',int(s[0]) + int(s[1]) + int(s[2]),'.\n')
        q = input('Press "y" if you want to repeat this step.\n')
    else:
        print('Please enter valid 3-digit number.\n')
        q = 'y'

# Дано целое число n. Выведите следующее за ним чётное число.

q = 'y'

while q == 'y':
    n = int(input('Please enter some integer. I will try to output next even integer.\n'))
    if n % 2 == 0:
        print('Next even integer is',n+2,'\n')
        q = input('Press "y" if you want to repeat this step.\n')
    else:
        print('Next even integer is', n + 1, '\n')
        q = input('Press "y" if you want to repeat this step.\n')

# Дано положительное действительное число X. Выведите его дробную часть.

q = 'y'

while q == 'y':
    x = float(input("Please enter some real number. I will try to output it's fraction.\n"))
    if x > 0:
        print("The fraction is ",x - x // 1,".\n")
        q = input('Press "y" if you want to repeat this step.\n')
    else:
        print("Hey! Make it positive!\n")
        q = input('Press "y" if you want to repeat this step.\n')

# Дано положительное действительное число X. Выведите его первую цифру после десятичной точки.

q = 'y'

while q == 'y':
    x = float(input("Please enter some real number. I will try to output it's first fraction's digit.\n"))
    if x > 0:
        print("The answer is",str(x - x// 1)[2])
        q = input('Press "y" if you want to repeat this step.\n')
    else:
        print("Hey! Make it positive!\n")
        q = input('Press "y" if you want to repeat this step.\n')
