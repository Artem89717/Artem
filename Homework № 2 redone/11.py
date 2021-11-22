# Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити)
dic = {'a': 10, 'w': 45, 'f': 43, 'g': 10, 's': 43, 'j': 45, 'z': 55, 'x': 11}
result = {}
for key, value in dic.items():
    if value not in result.values():
        result[key] = value

print(result)
