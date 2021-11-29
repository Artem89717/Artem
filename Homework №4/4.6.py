# Вводиться число. Якщо це число додатне, знайти його квадрат,
# якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
number = int(input("Уведіть число:  "))

if number > 0:
    number = number * number
    print(number)
if number < 0:
    number += 100
    print(number)
if number == 0:
    print(number)
