#Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
def myRange(*args):
    myList = []
    if len(args) == 1:
        k = 0
        if args[0] > 0:
            while k < args[0]:
                myList.append(k)
                k = k + 1
        else:
            while k > args[0]:
                myList.append(k)
                k = k - 1
    elif len(args) == 2:
        k = args[0]
        if args[0] < args[1]:
            while k < args[1]:
                myList.append(k)
                k = k + 1
        else:
            while k > args[1]:
                myList.append(k)
                k = k - 1
    else:
        k = args[0]
        if args[0] < args[1]:
            while k < args[1]:
                myList.append(k)
                k = k + args[2]
        else:
            while k > args[1]:
                myList.append(k)
                k = k + args[2]
    return myList
for i in myRange(0, 55):
    print(i)