#Створити програму-емулятор світлофора для авто і пішоходів.
#Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
#Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
#Приблизний результат роботи наступний:
#Red        Green
#Red        Green
#Red        Green
#Red        Green
#Yellow     Green
#Yellow     Green
#Green      Red
#Green      Red
#Green      Red
#Green      Red
#Yellow     Red
#Yellow     Red
#Red        Green
#.......
import time
print("Car       People")
print("")

while True:
    for i in range(5):
        print("Red          Green")
        time.sleep(1)

    for i in range(3):
        print("Yellow       Green")
        time.sleep(1)

    for i in range(7):
        print("Green         Red")
        time.sleep(1)

    for i in range(3):
        print("Yellow        Red")
        time.sleep(1)