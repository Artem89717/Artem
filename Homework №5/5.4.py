# Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100),
# кожен елемент якого буде ділитись без остачі на 5 але не буде ділитись на 3.
# Перевірка: [5, 10, 20, 25, 35, 40, 50, 55, 65, 70, 80, 85, 95]
arr = [num for num in range(100) if num % 5 == 0 and num % 3 != 0]
print(arr)
