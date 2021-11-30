# 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.

def same_elements(elements_list):

    used_elements_list = []

    for i in elements_list:
        if elements_list.count(i) != 1 and i not in used_elements_list:
            print(str(i) + " in list " + str(elements_list.count(i)))
            used_elements_list.append(i)

same_elements([2,5,5,6,7,8,'j','j','j','g'])
