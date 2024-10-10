import os
import sys


def _create_file(filename: str = 'default') -> None:
    """Создание файла в директории /home/ramazan/SDLC/prac_1/"""
    filepath = f'/home/ramazan/SDLC/prac_1/{filename}'
    if not os.path.exists(filepath):
        os.mknod(filepath)

    print(f'Новый файл создан: {filepath}')


def _write_data(filepath: str, input_data: str) -> None:
    """Запись данных в ранее созданный файл"""
    with open(filepath, 'w') as f:
        for row in input_data:
            f.write(row)

    print(f'Данные были записаны в файл: {filepath}')


def _read_data(filepath: str) -> None:
    """Вывод данных из файла"""
    print('Вывод данных из файла:')
    with open(filepath, 'r') as f:
        print(f.read())


def _delete_file(filepath: str) -> None:
    """Удаление файла"""
    try:
        os.remove(filepath)
        print(f'Файл {filepath} был удален')
    except Exception as e:
        print(e)


def file_operations():

    filename = input("Введите название файла: ")
    if filename == '':
        print('Имя файла не может быть пустой строкой')
        exit()

    _create_file(filename)

    # filepath = f'/home/ramazan/SDLC/prac_1/{filename}'

    # print('Введите данные для записи: ')
    # input_data = sys.stdin.readlines()

    # _write_data(filepath, input_data)

    # _read_data(filepath)

    # _delete_file(filepath)


# file_operations()