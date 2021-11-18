# Напишіть програму для перетворення десяткової системи в шістнадцяткову
arr = input().split(",")
arr = list(map(int, arr))
arr = list(map(hex, arr))
arr_result = []
for i in arr:
    arr_result.append(i[2:])

print(', '.join(arr_result))
