from random import randint
def get_name():
    vowel_letters = 'аеёиоуэюяэ'
    consonant_letters = 'бвгджзйклмнпрстфхцчшщ'
    result_name = ''
    for i in range(3, randint(4, 9)):
        result_name = result_name + vowel_letters[randint(0, 9)] + consonant_letters[randint(0, 19)]
    return result_name.title()

def get_phone_number():
    result_number = '8'
    for i in range(10):
        result_number = result_number + str(randint(0, 9))
    return result_number

def get_surname():
    vowel_letters = 'аеёиоуэюяэ'
    consonant_letters = 'бвгджзйклмнпрстфхцчшщ'
    surname_end = ['ан', 'ын', 'ин', 'ских', 'ов', 'ев', 'ской', 'цкой', 'их', 'ых', 'ая', 'ова', 'ева']
    result_name = ''
    for i in range(3,randint(4,9)):
        result_name = result_name + vowel_letters[randint(0, 9)] + consonant_letters[randint(0, 19)]
    result_name = result_name + surname_end[randint(0, 12)]
    return result_name.title()

def get_birthdate():
    result = f'{randint(1,31)}.{randint(1,12)}.{randint(1960,2010)}'
    return result


def get_job_city():
    city_list = ['Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Самара', 'Омск', 'Казань', 'Челябинск', 'Ростов-на-Дону',
                 'Уфа', 'Волгоград','Пермь','Красноярск','Воронеж','Саратов','Краснодар','Тольятти','Ижевск','Ульяновск','Барнаул','Владивосток','Ярославль',
                 'Иркутск','Тюмень','Махачкала','Хабаровск','Оренбург','Новокузнецк','Кемерово','Рязань','Томск','Астрахань','Пенза', 'Липецк',
                 'Тула','Киров','Чебоксары','Калининград','Брянск','Курск','Иваново','Магнитогорск','Улан-Удэ','Москва']
    result = city_list[randint(0,42)]
    return result


