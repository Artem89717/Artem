# Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран
list = ['t', 'i', 'a', 'e', '1', '16']
sent_str = ""
for i in list:
    sent_str += str(i)
print(sent_str)
