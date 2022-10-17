# -*- mode: python ; coding: utf-8 -*-
import telephone_book
start_text = 'Для того, чтобы выбрать действие введите нужную цифру\n' \
             '1 - Сгенерировать новый справочник и вывести на экран\n' \
             'Далее вы сможете экспортировать справочник в файл\n' \
             '2 - Импортировать справочник из файла и вывести на экран'
print(start_text)
user_choise = int(input('Введите число от 1 до 2: '))
while user_choise > 2 or user_choise < 1 :
    print('Выберите вариант 1 или 2')
    user_choise = int(input('Введите число от 1 до 2: '))
if user_choise == 1:
    N = int(input('Введите количество тысяч строк: '))
    t_book = telephone_book.get_telephone_book(N)
    print(t_book)
    print('Если необходимо сделать экспорт данного списка в файл выберите 1 если нет, 2')
    user_choise_2 = int(input('Введите число от 1 до 2: '))
    while user_choise_2 > 2 or user_choise_2 < 1:
        print('Выберите вариант 1 или 2')
        user_choise_2 = int(input('Введите число от 1 до 2: '))
        if user_choise_2 == 1:
            telephone_book.export_telephone_book(t_book)
            print('Справочник экспортирован в файл phone_book.csv')
        else:
            print('Справочник сгенерирован но не экспортирован')
else:
    name = input('Введите название файла из которого необходимо импортировать список в формате "filename.csv": ')
    telephone_book.import_telephone_book(name)