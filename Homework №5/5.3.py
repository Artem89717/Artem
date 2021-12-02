# На основі попередньої функції створити наступний кусок кода:
# а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
# б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
# Name: vasya
# Password: wasd
# Status: password must have at least one digit
# Name: vasya
# Password: vasyapupkin2000
# Status: OK
# P.S. Не забудьте використати блок try/except ;)
user_pass_list = [("Artem", "qww389457898"), ("Andrii", "qw86789698"),
                  ("Anton", "4er56r7867"), ("Artemii", "869959905"), ("Alex", "8699548586")]


class ShortLogin(Exception):
    pass


class LongLogin(Exception):
    pass


class ShortPass(Exception):
    pass


class NoDigit(Exception):
    pass


def validation(user_name, password):
    check = False
    for i in password:
        if i.isdigit() == True:
            check = True

    if len(user_name) < 3:
        raise ShortLogin('Довжина імені має бути >= 3')

    if len(user_name) > 50:
        raise LongLogin(' Довжина імені має бути <= 50')

    if len(password) < 8:
        raise ShortPass('Довжина пароля має бути >= 8')

    if check == False:
        raise NoDigit('Пароль має містити бодай 1 цифру')


def check_each_user():
    for i in user_pass_list:
        print("")
        print("Ім'я: " + i[0])
        print("Пароль: " + i[1])
        try:
            validation(i[0], i[1])
        except ShortLogin:
            print("Status: " + "Довжина імені має бути >= 3")
        except LongLogin:
            print("Status: " + "Довжина імені має бути <= 50")
        except ShortPass:
            print("Status: " + "Довжина пароля має бути >= 8")
        except NoDigit:
            print("Status: " + "Пароль має містити бодай 1 цифру")
        else:
            print("Status: OK")


check_each_user()
