# Створити цикл від 0 до ... (вводиться користувачем).
# В циклі створити умову, яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0.
number_from_user = int(input("Write a number: "))
for num in range(number_from_user):
    if num % 17 == 0:
        print(num)
