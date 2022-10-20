# -*- mode: python ; coding: utf-8 -*-

def open_base(file_name):  #Открытие базы данных
    file = open(file_name, "r", encoding="utf-8-sig")
    uni_base = file.readlines()
    return uni_base


def change_name(current_base, change_name_lst): #Замена имени
    base_line = current_base[change_name_lst[0]].split(';')
    base_line[1] = change_name_lst[1]
    base_line = ";".join(map(str, base_line))
    current_base[change_name_lst[0]] = base_line
    return current_base

def change_surname(current_base, change_surname_lst):   #Замена фамилии
    base_line = current_base[change_surname_lst[0]].split(';')
    base_line[2] = change_surname_lst[1]
    base_line = ";".join(map(str, base_line))
    current_base[change_surname_lst[0]] = base_line
    return current_base

def change_birth_date(current_base, change_birth_date_lst):  #Замена даты рождения
    base_line = current_base[change_birth_date_lst[0]].split(';')
    base_line[3] = change_birth_date_lst[1]
    base_line = ";".join(map(str, base_line))
    current_base[change_birth_date_lst[0]] = base_line
    return current_base

def change_phone_number(current_base, change_phone_number_lst):  #Замена телефона
    base_line = current_base[change_phone_number_lst[0]].split(';')
    base_line[4] = change_phone_number_lst[1]
    base_line = ";".join(map(str, base_line))
    current_base[change_phone_number_lst[0]] = base_line
    return current_base

def change_facultet(current_base, change_facultet_lst):      #Замена факультета
    base_line = current_base[change_facultet_lst[0]].split(';')
    base_line[5] = change_facultet_lst[1]
    base_line = ";".join(map(str, base_line))
    current_base[change_facultet_lst[0]] = base_line
    return current_base

def add_new_row(current_base,new_row_lst):      #Добавление новой записи
    new_id_string = current_base[-1].split(';')
    new_id = str(int(new_id_string[0]) + 1)
    result = f'{new_id};{new_row_lst[0]};{new_row_lst[1]};{new_row_lst[2]};{new_row_lst[3]};{new_row_lst[4]}'
    current_base.append(result)
    return current_base

def delete_row(current_base, number_of_row):         #Удаление записи и замена остальных id согласно нумерации
    current_base_list = []
    for i in current_base:
        i = i.split(';')
        current_base_list.append(i)
    current_base_list.pop(number_of_row)
    for j in range(number_of_row, len(current_base_list)):
        current_base_list[j][0] = str(j)
    for k in range(len(current_base_list)):
        current_base_list[k] = ";".join(map(str, current_base_list[k]))
        current_base = current_base_list
    return current_base

def save_base(current_base, file_name):          #Сохранение базы данных в файл
    file = open(file_name, "w", encoding="utf-8-sig")
    for i in current_base:
        file.writelines(i)

def show_base(current_base):       #Показать всю базу
    for line in current_base:
        print(line)

def show_row(current_base, row_number):  #Показать определенную строку из базы
    print(current_base[0])
    print(current_base[row_number])




