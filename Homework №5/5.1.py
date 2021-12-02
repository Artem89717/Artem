# Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
# Функція повинна приймати три аргументи: два - обов'язкових
# (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
# Логіка наступна:
# якщо введено коректну пару ім'я/пароль - вертається <True>;
# якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>,
# інакше (<silent> == <False>) - породжується виключення LoginException
def check_user(username, password, silent=False):
    user_list = [("Artem", 389457), ("Andrii", 86789698786876),
                 ("Anton", 4567867), ("Artemii", 869959905), ("Alex", 8699548586)]
    check_flag = False
    for i in user_list:
        if username in i and i[1] == password:
            print("True")
            check_flag = True
            return True

    if check_flag != True and silent == True:
        print("False")
        return False
    elif check_flag != True and silent == False:
        raise Exception('LoginException')


check_user("Artem", 38945789, True)
