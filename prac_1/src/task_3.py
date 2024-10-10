import os
import sys
import json


def _create_json(
        filepath: str,
        name: str,
        surname: str,
        group: str) -> None:
    """Создание json в директории /home/ramazan/SDLC/prac_1/"""
    if not os.path.exists(filepath):
        os.mknod(filepath)

    name = 'Ramazan' if name == '' else name
    surname = 'Sayanov' if surname  == '' else surname
    group = 'BFBO-01-21' if group == '' else group
    data = {'name': name, 'surname': surname, 'group': group}

    with open(filepath, 'w') as file:
        json.dump(data, file)

    print(f'Новый файл с данными создан: {filepath}')


def _read_json(filepath: str) -> None:
    """Вывод данных из json"""
    print('Вывод данных из json:')
    with open(filepath, 'r') as f:
        print(f.read())



def _delete_json(filepath: str) -> None:
    """Удаление json"""
    try:
        os.remove(filepath)
        print(f'json {filepath} был удален')
    except Exception as e:
        print(e)


def json_operations():

    filename = input("Введите название файла: ")
    if filename == '':
        print('Имя файла не может быть пустой строкой')
        exit()

    filepath = f'/home/ramazan/SDLC/prac_1/{filename}.json'

    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    group = input('Введите группу: ')

    _create_json(
        filepath,
        name,
        surname,
        group
    )

    print(f'Вывод данных из {filepath}')
    _read_json(filepath)

    _delete_json(filepath)




json_operations()