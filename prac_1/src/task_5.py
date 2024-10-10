import zipfile
import os
from task_2 import _create_file


def _create_zip_archive(zip_name: str) -> None:
    """Создание архива в директории /home/ramazan/SDLC/prac_1/"""
    archive_path = f'/home/ramazan/SDLC/prac_1/{zip_name}.zip'
    with zipfile.ZipFile(archive_path, 'w') as zipf:
        print(f"Новый архив создан: {archive_path}")

def _add_file_to_zip(
        zip_path: str,
        filepath: str) -> None:
    """Добавление файла в zip-архив"""
    with zipfile.ZipFile(zip_path, 'a') as zipf:
        zipf.write(filepath, os.path.basename(filepath))
        print(f"Файл '{filepath}' добавлен в архив.")

# zip_name = '/home/ramazan/SDLC/prac_1/test'
# filepath = '/home/ramazan/SDLC/prac_1/sdsd'
# _add_file_to_zip(zip_name, filepath)


def _extract_zip(
        zip_name: str,
        extract_to: str) -> None:
    """Разархивирование файлов и вывод информации"""
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_to)
        print(f"Архив '{zip_name}' разархивирован в '{extract_to}'")
        print("Содержимое архива:")
        for file_info in zipf.infolist():
            print(f"- {file_info.filename} ({file_info.file_size} байт)")


def _delete_file_and_zip(
        filepath: str,
        zip_path: str) -> None:
    """Удалаение файла и архива"""
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Файл '{filepath}' удален.")
    else:
        print(f"Файл '{filepath}' не существует.")

    if os.path.exists(zip_path):
        os.remove(zip_path)
        print(f"Архив '{zip_path}' удален.")
    else:
        print(f"Архив '{zip_path}' не существует.")

def archive_operations():
    zip_name = input("Введите имя архива: ")
    if zip_name == '':
        print('Имя архива не может быть пустой строкой')
        exit()

    _create_zip_archive(zip_name)
    zip_path = f'/home/ramazan/SDLC/prac_1/{zip_name}.zip'

    filename = input("Введите название файла: ")
    if filename == '':
        print('Имя файла не может быть пустой строкой')
        exit()

    _create_file(filename)
    filepath = f'/home/ramazan/SDLC/prac_1/{filename}'


    _add_file_to_zip(zip_path, filepath)

    extract_directory = "/home/ramazan/SDLC/prac_1/extracted_files"
    os.makedirs(extract_directory, exist_ok=True)
    _extract_zip(zip_path, extract_directory)

    _delete_file_and_zip(zip_path, filepath)

archive_operations()