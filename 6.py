# Напишіть програму для перевірки наступного: чи міститься вказане значення в зазначеній групі значень
def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False


print(is_group_member([1, 5, 8, 3, 17, 16, 34, 22], 76))
print(is_group_member([5, 8, 3, 14, 17, 22, 33], 33))
