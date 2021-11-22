# Написати скрипт, який видалить пусті елементи із списка
def Remove(list):
    list = [t for t in list if t]
    return list


list = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
print(Remove(list))
