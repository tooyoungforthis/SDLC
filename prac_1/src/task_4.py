import xml.etree.ElementTree as ET
import os
import sys

def _create_xml(
        filepath: str) -> None:
    """Создание json в директории /home/ramazan/SDLC/prac_1/"""
    root = ET.Element("data")
    tree = ET.ElementTree(root)
    tree.write(filepath)
    print(f"Новый XML файл создан: {filepath}")


def _write_data(
        filepath: str,
        input_data: str) -> None:
    root = ET.parse(filepath).getroot()
    entry = ET.SubElement(root, "entry")
    entry.text = input_data

    tree = ET.ElementTree(root)
    tree.write(filepath)
    print("Данные были записаны в файл")

def _read_xml(filepath: str) -> None:
    """Вывод данных из файла"""
    print('Вывод данных из файла:')
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
    except Exception as e:
        print(e)

    for entry in root.findall('entry'):
        print(entry.text)

def _delete_xml(filepath: str) -> None:
    """Удаление файла"""
    try:
        os.remove(filepath)
        print(f'Файл {filepath} был удален')
    except Exception as e:
        print(e)


def xml_operations():
    filename = input("Введите название файла: ")
    if filename == '':
        print('Имя файла не может быть пустой строкой')
        exit()

    filepath = f'/home/ramazan/SDLC/prac_1/{filename}.xml'
    _create_xml(filepath)

    print('Введите данные для записи: ')
    input_data = input()

    _write_data(filepath, input_data)

    _read_xml(filepath)

    _delete_xml(filepath)


xml_operations()