#  Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата,
#  і вертатиме 3 значення (кортеж): периметр квадрата, площа квадрата та його діагональ.
from math import sqrt


def square(side):
    perimetr = side * 4
    area = side ** 2
    diagonal = side * sqrt(2)
    return (perimetr, area, diagonal)


result = square(int(input("Введіть сторону квадрата: ")))
print(result)
