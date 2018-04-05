# Задание 1

# Определите является ли строка записью числа.

q = 'y'

while q == 'y':
    s = input('Please enter a string. I will try to define if it is a number.\n')

    if s.isdigit():
        print("Yes, it's a number.\n")

    else:
        print("No, it is not a number.\n")

    q = input('Press "y" if you want to repeat this step.\n')

# Посчитайте сколько у вас пробелов в строке.

q = 'y'

while q == 'y':
    s = input('Please enter a string. I will try to count how many spaces does it contain.\n')
    print("Your string contains", s.count(' '), "space(s).")
    q = input('Press "y" if you want to repeat this step.\n')

# Посчитайте сколько у вас символов точки '.' в строке.

q = 'y'

while q == 'y':
    s = input('Please enter a string. I will try to count how many points does it contain.\n')
    print("Your string contains", s.count('.'), "point(s).")
    q = input('Press "y" if you want to repeat this step.\n')

# Создайте строку "Homework". Преобразуйте ее в строку длиной 100 символов,
# посередине которой исходное слово, а с обеих сторон строка заполнена
# пробелами. Выведите ее на экран.

print("""Now we'll perform some magic with a word "Homework". Here we go:\n""")
print('Homework'.center(100),"\n")

# Сделайте первые буквы слов строки большими (upper case).

q = 'y'

while q == 'y':
    s = input('Please enter a string. I will try to make first letters of each word uppercase\n(all other will be lowercase).\n')
    print(s.title())
    q = input('Press "y" if you want to repeat this step.\n')