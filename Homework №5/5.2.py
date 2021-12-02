# Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
# - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
# - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
# Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
def validation(user_name, password):
    check = False
    for i in password:
        if i.isdigit() == True:
            check = True

    if len(user_name) < 3:
        raise Exception('Довжина імені має бути >= 3')

    if len(user_name) > 50:
        raise Exception(' Довжина імені має бути <= 50')

    if len(password) < 8:
        raise Exception('Довжина пароля має бути >= 8')

    if check == False:
        raise Exception('Пароль має містити бодай 1 цифру')


validation("Artem", "metra123xgeegx")
