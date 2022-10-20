# -*- mode: python ; coding: utf-8 -*-
import operations
import UI

process = True

UI.start_message()                                          # Стартовое сообщение
base = operations.open_base(UI.open_base_message())         # Первое открытие базы

while process == True:
    choise = UI.choise_message()                            # Выбор действия
    if choise == 1:                                         # Открыть другую базу данных
        base = operations.open_base(UI.open_base_message())
    elif choise == 2:                                       # Вывод в консоль текущую открытую базу данных
        operations.show_base(base)
    elif choise == 3:                                       # Вывод в консоль определенной строки
        operations.show_row(base, UI.show_row_message())
    elif choise == 4:                                       # Выбор параметра для замены
        parameter = UI.show_change_parameter()
        if parameter == 1:                                                             # Замена имени
            base = operations.change_name(base, UI.show_change_name())
        elif parameter == 2:                                                           # Замена фамилии
            base = operations.change_surname(base, UI.show_change_surname())
        elif parameter == 3:                                                           # Замена даты рождения
            base = operations.change_birth_date(base, UI.show_change_birth_date())
        elif parameter == 4:                                                           # Замена номера телефона
            base = operations.change_phone_number(base, UI.show_change_phone_number())
        elif parameter == 5:                                                           # Замена факультета
            base = operations.change_facultet(base, UI.show_change_facultet())
        else:
            print('')
    elif choise == 5:                                        # Добавление новой строки
        base = operations.add_new_row(base, UI.show_new_row())
    elif choise == 6:                                        # Удаление определенной строки
        base = operations.delete_row(base, UI.show_delete_row())
    elif choise == 7:                                        # Сохранение базы данных
        operations.save_base(base, UI.show_save_base())
    else:                                                    # Выход
        exit()

