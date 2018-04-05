# Пользователь вводит целое число. Требуется определить, является ли год с данным номером
# високосным. Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в
# соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но
# не кратен 100, а также если он кратен 400.

y = int(input(""" — Hey, Doc!
 — Hey, Marty! Are you ready? We are going to [please enter a year]!\n"""))

if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print("Oh no! This is a leap year! We are stuck!.. I mean YES!")
else:
    print("Well, nothing interesting here. Let's go back... I mean NO!")