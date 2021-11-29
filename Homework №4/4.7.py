# 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.

def same_elements(elements_string):
    elements_list = []
    used_elements_list = []
    for i in elements_string:
        elements_list.append(i)

    for i in elements_list:
        if elements_list.count(i) != 1 and i not in used_elements_list:
            print(i + " in list " + str(elements_list.count(i)))
            used_elements_list.append(i)

same_elements("jygoutci7675875rx87tc975f79uogtvo7iy6f7585374rtfy8itf654875")
