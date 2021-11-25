# Калькулятор
def calculations(number_1, operation, number_2):
    operation_list = ["+", "-", "/", "*"]
    if number_1.isdigit() and number_2.isdigit() and operation in operation_list and int(number_2) != 0:
        number_1 = int(number_1)
        number_2 = int(number_2)

        if operation == '+':
            print('{} + {} = '.format(number_1, number_2))
            print(number_1 + number_2)

        if operation == '-':
            print('{} - {} = '.format(number_1, number_2))
            print(number_1 - number_2)

        if operation == '*':
            print('{} * {} = '.format(number_1, number_2))
            print(number_1 * number_2)

        if operation == '/':
            print('{} / {} = '.format(number_1, number_2))
            print(number_1 / number_2)
    else:
        print('You have not typed a valid operator, please run the program again.')


def calculate():
    number_1 = input("Write number_1: ")
    operation = input("Write operation to do: ")
    number_2 = input("Write number_2: ")
    calculations(number_1, operation, number_2)


calculate()
