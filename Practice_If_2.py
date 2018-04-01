# Выведите сообщение "Correct number", если введённое число 0 < x <= 100, а
# если нет, то сообщение "Incorrect number"

n = int(input('Please enter a number:\n'))
if n>0 and n<=100:
    print('Correct number.')
else:
    print('Incorrect number.')