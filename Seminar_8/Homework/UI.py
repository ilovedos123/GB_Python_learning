# -*- mode: python ; coding: utf-8 -*-

def start_message():
    print('Перед началом работы необходимо открыть базу данных')
    print('_____________________________________________________')

def open_base_message():
    name = input('Введите имя файла базы данных в формате "name.csv": ')
    return name

def choise_message():
    print('_____________________________________________________________')
    print('Выберите необходимое действие:\n'
          '1: Открыть другую базу данных\n'
          '2: Вывод на экран текущей базы данных\n'
          '3: Вывод на экран определенной строки из текущей базы данных\n'
          '4: Изменить параметр базы данных\n'
          '5: Добавить новую запись в текущую базу данных\n'
          '6: Удалить запись из текущей базы данных\n'
          '7: Сохранить базу данных\n'
          '8: Завершение работы')
    print('_____________________________________________________________')
    choise = int(input('Введите ваш вариант: '))
    while choise > 8 or choise < 1:
        choise = int(input('Введите вариант от 1 до 8: '))
    return choise

def show_row_message():
    row = int(input('Введите id записи для показа: '))
    return row

def show_change_parameter():
    # global parameter
    print('_____________________________________________')
    print('Выберите какой параметр необходимо изменить:\n'
          '1: Имя\n'
          '2: Фамилия\n'
          '3: Дата рождения\n'
          '4: Номер телефона\n'
          '5: Факультет\n'
          '6: Вернуться в главное меню')
    print('_____________________________________________')
    parameter = int(input('Введите вариант от 1 до 6: '))
    while parameter > 6 or parameter < 1:
        parameter = int(input('Введите вариант от 1 до 6: '))
    return parameter

def show_change_name():
    change_name_list = []
    name_id = int(input('Для замены параметра "Имя" введите id строки: '))
    new_name = input('Введите новое имя: ')
    change_name_list.append(name_id)
    change_name_list.append(new_name)
    return change_name_list

def show_change_surname():
    change_surname_list = []
    surname_id = int(input('Для замены параметра "Фамилия" введите id строки: '))
    new_surname = input('Введите новую фамилию: ')
    change_surname_list.append(surname_id)
    change_surname_list.append(new_surname)
    return change_surname_list

def show_change_birth_date():
    change_birth_date_list = []
    birth_date_id = int(input('Для замены параметра "Дата рождения" введите id строки: '))
    new_birth_date = input('Введите новую дату рождения: ')
    change_birth_date_list.append(birth_date_id)
    change_birth_date_list.append(new_birth_date)
    return change_birth_date_list

def show_change_phone_number():
    change_phone_number_list = []
    phone_number_id = int(input('Для замены параметра "Номер телефона" введите id строки: '))
    new_phone_number = input('Введите новый номер телефона: ')
    change_phone_number_list.append(phone_number_id)
    change_phone_number_list.append(new_phone_number)
    return change_phone_number_list

def show_change_facultet():
    change_facultet_list = []
    facultet_id = int(input('Для замены параметра "Факультет" введите id строки: '))
    new_facultet = input('Введите новый факультет: ')
    change_facultet_list.append(facultet_id)
    change_facultet_list.append(new_facultet)
    return change_facultet_list

def show_new_row():
    new_row_list = []
    add_name = input('Введите параметр "Имя" новой записи: ')
    new_row_list.append(add_name)
    add_surname = input('Введите параметр "Фамилия" новой записи: ')
    new_row_list.append(add_surname)
    add_birth_date = input('Введите параметр "Дата рождения" новой записи: ')
    new_row_list.append(add_birth_date)
    add_phone_number = input('Введите параметр "Номер телефона" новой записи: ')
    new_row_list.append(add_phone_number)
    add_facultet = input('Введите параметр "Факультет" новой записи: ')
    new_row_list.append(add_facultet)
    return new_row_list

def show_delete_row():
    delete_row_id = int(input('Для удаления записи введите id строки: '))
    return delete_row_id

def show_save_base():
    save_file_name = input('Введите имя файла для сохранения базы данных в формате "name.csv": ')
    return save_file_name


