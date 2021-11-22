# Написати скрипт, який пройдеться по списку, який складається із кортежів,
# і замінить для кожного кортежа останнє значення
list_of_list = [(90, 60, 33, 45, 175), (55, 60, 700, 98), (55, 3, 17), (45,), (77, 99)]
list_of_list = list(map(list, list_of_list))
from_input = input()

for i in list_of_list:
    i[-1] = from_input

list_of_tuple = list(map(tuple, list_of_list))
print(list_of_list)
