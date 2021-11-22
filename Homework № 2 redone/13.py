# Написати скрипт, який отримає максимальне і мінімальне значення із словника
dic = {3: 300, 6: 600, 7: 809, 8: 907, 4: 178, 1: 450}
min_key = min(dic, key=dic.get)
max_key = max(dic, key=dic.get)
print('Max: ', dic.get(max_key))
print('Min: ', dic.get(min_key))
