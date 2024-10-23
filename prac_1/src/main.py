import os
import sys
import psutil
import json
import zipfile
from psutil._common import bytes2human
import xml.etree.ElementTree as ET


def is_in_current_directory(filepath):
    abs_path = os.path.abspath(filepath)
    return os.path.commonpath([os.getcwd(), abs_path]) == os.getcwd()

def output_info() -> None:
    """Вывод основной информации

    device: Имя партиции диска
    mountpoint: Точка монтирования — это каталог или файл, c помощью которого
                обеспечивается доступ к новой файловой системе, каталогу или файлу
    fstype: Тип файловой системы
    opts: Различные доступные опции. Зависит от платформы
    """
    templ = "%-17s %8s %8s %8s %5s%%  %13s  %s"
    print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
                   "Mount"))
    for part in psutil.disk_partitions(all=True):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                # пропускаем приводы cd-rom, в которых нет диска;
                # они могут вызвать ошибку графического интерфейса
                # Windows для неготового раздела или просто зависнуть
                continue
        usage = psutil.disk_usage(part.mountpoint)
        print(templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint))


def _create_file(filename: str) -> None:
    """Создание файла в директории /home/ramazan/SDLC/prac_1/"""
    filepath = f'/home/ramazan/SDLC/prac_1/{filename}'
    if not os.path.exists(filepath):
        os.mknod(filepath)

    print(f'Новый файл создан: {filepath}')


def _write_data(filename: str, input_data: str) -> None:
    """Запись данных в ранее созданный файл"""
    filepath = f'/home/ramazan/SDLC/prac_1/{filename}'
    try:
        with open(filepath, 'w') as f:
            for row in input_data:
                f.write(row)

        print(f'Данные были записаны в файл: {filepath}')
    except Exception as e:
        print(e)


def _read_file(filename: str) -> None:
    """Вывод данных из файла"""
    filepath = f'/home/ramazan/SDLC/prac_1/{filename}'
    print(F'Вывод данных из файла: {filepath}')
    try:
        with open(filepath, 'r') as f:
            print(f.read())
    except Exception as e:
        print(e)



def _delete_file(filename: str) -> None:
    """Удаление файла"""
    filepath = f'/home/ramazan/SDLC/prac_1/{filename}'
    try:
        os.remove(filepath)
        print(f'Файл {filepath} был удален')
    except Exception as e:
        print(e)


def _create_json(
        filename: str,
        name: str,
        surname: str,
        group: str) -> None:
    """Создание json в директории /home/ramazan/SDLC/prac_1/"""
    filepath = f'/home/ramazan/SDLC/prac_1/{filename}.json'
    if not os.path.exists(filepath):
        os.mknod(filepath)

    name = 'Ramazan' if name == '' else name
    surname = 'Sayanov' if surname  == '' else surname
    group = 'BFBO-01-21' if group == '' else group
    data = {'name': name, 'surname': surname, 'group': group}

    with open(filepath, 'w') as file:
        json.dump(data, file)

    print(f'Новый файл с данными создан: {filepath}')


def _read_json(filename: str) -> None:
    """Вывод данных из json"""
    filepath = f'/home/ramazan/SDLC/prac_1/{filename}.json'
    try:
        print('Вывод данных из json:')
        with open(filepath, 'r') as fn:
            data = json.load(fn)
            print(data)
            # try:
            #     print(f"Имя: {data['name']}")
            #     print(f"Фамилия: {data['surname']}")
            #     print(f"Группа: {data['group']}")
            # except Exception as e:
            #     print(e)
    except Exception as e:
        print(e)

def _delete_json(filename: str) -> None:
    """Удаление json"""
    filepath = f'/home/ramazan/SDLC/prac_1/{filename}.json'
    try:
        os.remove(filepath)
        print(f'json {filepath} был удален')
    except Exception as e:
        print(e)


def _create_xml(filename: str) -> None:
    """Создание xml в директории"""
    filepath = f'/home/ramazan/SDLC/prac_1/{filename}.xml'
    root = ET.Element("data")
    tree = ET.ElementTree(root)
    tree.write(filepath)
    print(f"Новый XML файл создан: {filepath}")


def _write_data_xml(
        filename: str,
        input_data: str) -> None:
    """Запись данных в xml"""

    try:
        filepath = f'/home/ramazan/SDLC/prac_1/{filename}.xml'
        root = ET.parse(filepath).getroot()

        for k, v in input_data.items():
            item = ET.SubElement(root, "Item")
            item.attrib["id"] = k
            item.text = v

        tree = ET.ElementTree(root)
        tree.write(filepath)
        print("Данные были записаны в файл")
    except Exception as e:
        print(e)

def _read_xml(filename: str) -> None:
    """Вывод данных из файла"""
    print('Вывод данных из файла:')
    filepath = f'/home/ramazan/SDLC/prac_1/{filename}.xml'
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()

        for entry in root.findall("Item"):
            k = entry.attrib["id"]
            v = entry.text
            print(f'{k}: {v}')

    except Exception as e:
        with open(filepath, 'r', encoding='utf-8') as file:
            xml_string = file.read()
            print(xml_string)


def _delete_xml(filepath: str) -> None:
    """Удаление файла"""
    filepath = f'/home/ramazan/SDLC/prac_1/{filename}.xml'
    try:
        os.remove(filepath)
        print(f'Файл {filepath} был удален')
    except Exception as e:
        print(e)


def _create_zip_archive(zipname: str) -> None:
    """Создание архива в директории /home/ramazan/SDLC/prac_1/"""
    zip_path = f'/home/ramazan/SDLC/prac_1/{zipname}.zip'
    try:
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            print(f"Новый архив создан: {zip_path}")
    except Exception as e:
        print(e)

def _add_file_to_zip(
        zipname: str,
        filename: str) -> None:
    """Добавление файла в zip-архив"""
    zip_path = f'/home/ramazan/SDLC/prac_1/{zipname}.zip'
    filepath = f'/home/ramazan/SDLC/prac_1/{filename}'

    if not os.path.exists(zip_path):
        print('Такого архива не существует')
        return

    try:
        with zipfile.ZipFile(zip_path, 'a') as zipf:
            zipf.write(filepath, os.path.basename(filepath))
            print(f"Файл '{filepath}' добавлен в архив.")
    except Exception as e:
        print(e)

# zip_name = '/home/ramazan/SDLC/prac_1/test'
# filepath = '/home/ramazan/SDLC/prac_1/sdsd'
# _add_file_to_zip(zip_name, filepath)


def _extract_zip(
        zipname: str,
        extract_to: str) -> None:
    """Разархивирование файлов и вывод информации"""

    zip_path = f'/home/ramazan/SDLC/prac_1/{zipname}.zip'
    if not os.path.exists(zip_path):
        print('Такого архива не существует')
        return

    ext_path = f'/home/ramazan/SDLC/prac_1/{extract_to}'

    try:
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(ext_path)
            print(f"Архив '{zip_path}' разархивирован в '{ext_path}'")
            print("Содержимое архива:")
            for file_info in zipf.infolist():
                print(f"- {file_info.filename} ({file_info.file_size} байт)")
    except Exception as e:
        print(e)


def _delete_zip(zip_name: str) -> None:
    """Удаление архива"""
    zip_path = f'/home/ramazan/SDLC/prac_1/{zip_name}.zip'
    if os.path.exists(zip_path):
        os.remove(zip_path)
        print(f"Архив '{zip_path}' удален.")
    else:
        print(f"Архив '{zip_path}' не существует.")



print('Добро пожаловать в мою программу')
print('Список возможных действий:')
print('1: Вывести информацию в консоль о логических дисках, именах, метке тома, размере и типе файловой системы')
print('2: Создать файл')
print('3: Записать в файл строку, введённую пользователем')
print('4: Прочитать файл в консоль')
print('5: Удалить файл')
print('6: Создать файл формате JSON в любом редакторе или с использованием данных, введенных пользователем')
print('7: Прочитать JSON в консоль')
print('8: Удалить JSON')
print('9: Создать файл формате XML из редактора')
print('10: Записать в XML новые данные из консоли')
print('11: Прочитать XML в консоль')
print('12: Удалить XML')
print('13: Создать архив в форматер zip')
print('14: Добавить файл, выбранный пользователем, в архив')
print('15: Разархивировать архив и вывести данные о нем')
print('16: Удалить архив')
print('Введите exit для выхода из программы')
print('=' * 100)

while True:

    action = input('Выберите действие (1-16/exit): ')
    if action not in [str(i) for i in list(range(1, 17))] + ['exit']:
        print('Неправильный ввод, выберите корректное действие')
        continue
    if action == 'exit':
        print('Окончание работы программы')
        exit()

    if action == '1':
        output_info()

    if action == '2':
        filename = input("Введите название файла для создания: ")
        if filename == '':
            print('Имя файла не может быть пустой строкой')
            continue
        if not is_in_current_directory(filename):
            print("Ошибка: файл находится вне текущей директории.")
            continue
        _create_file(filename)

    if action == '3':
        filename = input('Выберите файл для записи: ')
        if filename == '':
            print('Имя файла не может быть пустой строкой')
            continue
        if not is_in_current_directory(filename):
            print("Ошибка: файл находится вне текущей директории.")
            continue
        print('Введите данные для записи: ')
        input_data = sys.stdin.readlines()
        _write_data(filename, input_data)

    if action == '4':
        filename = input('Выберите файл для прочтения: ')
        if filename == '':
            print('Имя файла не может быть пустой строкой')
            continue
        if not is_in_current_directory(filename):
            print("Ошибка: файл находится вне текущей директории.")
            continue
        _read_file(filename)


    if action == '5':
        filename = input('Выберите файл для удаления: ')
        if filename == '':
            print('Имя файла не может быть пустой строкой')
            continue
        if not is_in_current_directory(filename):
            print("Ошибка: файл находится вне текущей директории.")
            continue
        _delete_file(filename)

    if action == '6':
        filename = input('Введите название json для создания: ')
        if filename == '':
            print('Имя json не может быть пустой строкой')
            continue
        if not is_in_current_directory(filename):
            print("Ошибка: файл находится вне текущей директории.")
            continue
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        group = input('Введите группу: ')
        _create_json(filename, name, surname, group)

    if action == '7':
        filename = input('Введите название json для прочтения: ')
        if filename == '':
            print('Имя json не может быть пустой строкой')
            continue
        if not is_in_current_directory(filename):
            print("Ошибка: файл находится вне текущей директории.")
            continue
        _read_json(filename)

    if action == '8':
        filename = input('Введите название json для удаления: ')
        if filename == '':
            print('Имя json не может быть пустой строкой')
            continue
        if not is_in_current_directory(filename):
            print("Ошибка: файл находится вне текущей директории.")
            continue
        _delete_json(filename)

    if action == '9':
        filename = input('Введите название xml для создания: ')
        if filename == '':
            print('Имя xml не может быть пустой строкой')
            continue
        if not is_in_current_directory(filename):
            print("Ошибка: файл находится вне текущей директории.")
            continue
        _create_xml(filename)

    if action == '10':
        filename = input('Введите xml для записи данных: ')
        if filename == '':
            print('Имя xml не может быть пустой строкой')
            continue
        if not is_in_current_directory(filename):
            print("Ошибка: файл находится вне текущей директории.")
            continue
        _id = input('Введите новый id записи: ')
        _item = input('Введите данные для записи: ')
        try:
            input_data = {_id: _item}
        except Exception as e:
            print('Введены неверные данные для записи')
            continue
        _write_data_xml(filename, input_data)

    if action == '11':
        filename = input('Введите xml для вывода данных: ')
        if filename == '':
            print('Имя xml не может быть пустой строкой')
            continue
        if not is_in_current_directory(filename):
            print("Ошибка: файл находится вне текущей директории.")
            continue
        _read_xml(filename)

    if action == '12':
        filename = input('Введите xml для записи данных: ')
        if filename == '':
            print('Имя xml не может быть пустой строкой')
            continue
        if not is_in_current_directory(filename):
            print("Ошибка: файл находится вне текущей директории.")
            continue
        _delete_xml(filename)

    if action == '13':
        arhcname = input('Введите имя архива для создания: ')
        if arhcname == '':
            print('Имя архива не может быть пустой строкой')
            continue
        if not is_in_current_directory(arhcname):
            print("Ошибка: архив находится вне текущей директории.")
            continue
        _create_zip_archive(arhcname)

    if action == '14':
        arhcname = input('Введите имя архива для добваления файла в него: ')
        if arhcname == '':
            print('Имя архива не может быть пустой строкой')
            continue
        if not is_in_current_directory(arhcname):
            print("Ошибка: архив находится вне текущей директории.")
            continue
        filename = input('Введите имя файла для добавления в архив: ')
        if filename == '':
            print('Имя файла не может быть пустой строкой')
            continue
        if not is_in_current_directory(filename):
            print("Ошибка: файл находится вне текущей директории.")
            continue
        _add_file_to_zip(arhcname, filename)

    if action == '15':
        arhcname = input('Введите имя архива для разархивирования: ')
        if arhcname == '':
            print('Имя архива не может быть пустой строкой')
            continue
        if not is_in_current_directory(arhcname):
            print("Ошибка: архив находится вне текущей директории.")
            continue

        ext_folder = input('Введите директорию для разархивирования: ')
        if ext_folder == '':
            print('Директория для разархивирования')
            continue
        if not is_in_current_directory(ext_folder):
            print("Ошибка: директория вне текущей директории.")
            continue

        _extract_zip(arhcname, ext_folder)

    if action == '16':
        arhcname = input('Введите имя архива для удаления: ')
        if arhcname == '':
            print('Имя архива не может быть пустой строкой')
            continue
        if not is_in_current_directory(arhcname):
            print("Ошибка: архив находится вне текущей директории.")
            continue
        _delete_zip(arhcname)























