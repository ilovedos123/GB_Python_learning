import generator
def export_telephone_book(phone_book):
    phone_book = list(phone_book.split())
    with open(r"phone_book.csv", "w") as file:
        count = 0
        while count < len(phone_book):
            file.write(f'{phone_book[count]} {phone_book[count+1]} {phone_book[count+2]} {phone_book[count+3]} {phone_book[count+4]} {phone_book[count+5]}''\n')
            count = count + 6

def get_telephone_book(number_of_rows):
        telephone_book = ''
        for i in range(1, number_of_rows*1000 + 1):
            telephone_book = telephone_book + f'{i} {generator.get_name()} {generator.get_surname()} {generator.get_birthdate()} {generator.get_job_city()} {generator.get_phone_number()}\n'
        return telephone_book

def import_telephone_book(file_name):
    with open(file_name, "r") as file:
        for line in file:
            print(line)


