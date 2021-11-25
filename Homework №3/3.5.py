# Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
# Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), п
# пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних "х" та "у"
# повертали рiзницю чисел.
# -  Повиннi опрацювати такi умови:
# -  x > y;       вiдповiдь - х бiльше нiж у на z
# -  x < y;       вiдповiдь - у бiльше нiж х на z
# -  x == y.      вiдповiдь - х дорiвнює z
def compare(x, y):
    if x > y:
        print("х > у on " + str(x - y))
        print(str(x) + " > " + str(y) + " on " + str(x - y))

    if x < y:
        print("у > х on " + str(y - x))
        print(str(y) + " > " + str(x) + " on " + str(y - x))

    if x == y:
        print("х = z")
        print(str(x) + " = " + str(y))

x = int(input('Write x: '))
y = int(input('Write y: '))

compare(x,y)