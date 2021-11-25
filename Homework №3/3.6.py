# Маємо рядок "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345"
# Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
# -  якщо довжина бульше 50 - > ваша фантазiя
def check_funk(str_input):
    letters_numbers = []
    letters = []
    numbers = []

    for i in str_input:
        letters_numbers.append(i)
    for i in letters_numbers:
        if i.isdigit():
            numbers.append(int(i))
        else:
            letters.append(i)

    if len(str_input) > 30 and len(str_input) < 50:
        print(len(str_input))
        print(len(letters))
        print(len(numbers))

    if len(str_input) <= 30:
        print(sum(numbers))
        print("".join(letters))

    if len(str_input) > 50:
        Vowels = 0
        Consonant = 0
        for i in letters:
            letter = i.lower()
            if letter == "a" or letter == "e" or \
                    letter == "i" or letter == "o" or \
                    letter == "u" or letter == "y":
                Vowels += 1
            else:
                Consonant += 1
        print("glasnye %i\n soglasnye %i" % (Vowels, Consonant))


check_funk("jghjktu8769598gjokt54jqlhvlhvlhbl;iubjh;iu;oub")
