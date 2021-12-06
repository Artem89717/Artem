# Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
# Функція повинна приймати три аргументи: два - обов'язкових
# (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
# Логіка наступна:
# якщо введено коректну пару ім'я/пароль - вертається <True>;
# якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>,
# інакше (<silent> == <False>) - породжується виключення LoginException
def check_user(username, password, silent=False):
    list = [("Artem", 389457), ("Andrii", 86789698786876),
            ("Anton", 4567867), ("Artemii", 869959905), ("Vlad", 8699548586)]
    checkflag = False
    for i in list:
        if username == i[0] and i[1] == password:
            print("True")
            checkflag = True
            return True

    if checkflag != True and silent == True:
        print("False")
        return False
    elif checkflag != True and silent == False:
        raise Exception('LoginException')


check_user(389457, 389457)
