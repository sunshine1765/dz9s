
from csv import DictReader, DictWriter
from os.path import exists

file_name = 'phones.csv'
file1_name = 'copy.csv'

class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_info():
    first_name = None
    is_valid_name = False

    while not is_valid_name:
        first_name = input('Введите имя: ')

        if len(first_name) == 0:
            print('Вы не ввели имя')
        else:
            is_valid_name = True

    last_name = input('Введите Фамилию: ')

    phone_number = None
    is_valid_phone = False

    while not is_valid_phone:
        try:
            phone_number = int(input('Введите номер: '))

            if len(str(phone_number)) != 11:
                raise LenNumberError('Не верная длина номера')
            else:
                is_valid_phone = True
        except ValueError:
            print('Не валидный номер')
        except LenNumberError as err:
            print(err)
            continue
        with open('phones.csv', 'r', encoding="UTF-8") as file:
            data = file.readlines()
        number_str = len(data)

    return [number_str, first_name, last_name, phone_number]


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def write_file(lst):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)

    for el in res:
        if el['Телефон'] == str(lst[2]):
            print('Такой телефон уже есть в справочнике')
            return

    obj = {'Номер_Строки': lst[0], 'Имя': lst[1], 'Фамилия': lst[2], 'Телефон': lst[3]}

    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        res.append(obj)
        f_writer = DictWriter(data, fieldnames=['Номер_Строки','Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
    return list(f_reader)


def copy_file(file_name, file1_name, number_str):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = data.readlines()
    string = f_reader[number_str]
    with open(file1_name, 'a', encoding='utf-8', newline='') as data:
        data.write(string)


def main():
    while True:
        command = input('Введите команду: ')

        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(get_info())
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует')
                continue
            print(*read_file(file_name))
        elif command == 'c':
            if not exists(file1_name):
                create_file(file1_name)
            if not exists(file_name):
                create_file(file_name)
            numbers_str = int(input("Введите номер строки которой надо скопировать: "))
            copy_file(file_name, file1_name, numbers_str)

main()
