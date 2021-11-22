# Написати скрипт, який отримує від користувача позитивне ціле число і створює словник,
# з ключами від 0 до введеного числа
number = int(input("Input a number "))
dict_result = {}

for x in range(number + 1):
    dict_result[x] = x * x

print(dict_result)
