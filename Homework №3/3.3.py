# Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12),
# яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)
season = {
    12: 'Winter', 1: 'Winter', 2: 'Winter',
    3: 'Spring', 4: 'Spring', 5: 'Spring',
    6: 'Summer', 7: 'Summer', 8: 'Summer',
    9: 'Autumn', 10: 'Autumn', 11: 'Autumn',

}


def seasons():
    number_for_user = int(input("Write a number: "))
    print(season[number_for_user])


seasons()
