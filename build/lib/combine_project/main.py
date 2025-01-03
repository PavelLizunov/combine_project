import os
import sys
import argparse

def is_text_file(file_path, text_extensions):
    """
    Проверяет, является ли файл текстовым по его расширению.
    """
    _, ext = os.path.splitext(file_path)
    return ext.lower() in text_extensions

def combine_project(root_dir, output_file, exclude_dirs=None, text_extensions=None):
    """
    Объединяет все текстовые файлы проекта в один файл с заголовками.

    :param root_dir: Корневая директория проекта.
    :param output_file: Имя выходного файла.
    :param exclude_dirs: Список директорий для игнорирования.
    :param text_extensions: Список текстовых расширений файлов.
    """
    if exclude_dirs is None:
        exclude_dirs = ['.git', '__pycache__', 'venv', 'node_modules']
    if text_extensions is None:
        text_extensions = ['.py', '.js', '.html', '.css', '.json', '.md', '.txt']

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for subdir, dirs, files in os.walk(root_dir):
            # Игнорируем указанные директории
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                file_path = os.path.join(subdir, file)
                if is_text_file(file_path, text_extensions):
                    relative_path = os.path.relpath(file_path, root_dir)
                    outfile.write(f'\n\n# Файл: {relative_path}\n')
                    outfile.write('#' + '=' * (len(relative_path) + 7) + '\n')
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            outfile.write(content)
                    except Exception as e:
                        outfile.write(f'# Не удалось прочитать файл: {e}\n')
    print(f'Все текстовые файлы проекта успешно объединены в {output_file}')

def main():
    """
    Точка входа для утилиты combine-project.
    """
    parser = argparse.ArgumentParser(
        prog='combine-project',
        description='Объединяет все текстовые файлы проекта в один файл.'
    )

    # Основные аргументы
    parser.add_argument(
        'project_dir',
        nargs='?',
        help='Путь к корневой директории проекта. Используйте "help" для подробной справки.'
    )
    parser.add_argument(
        'output_file',
        nargs='?',
        help='Имя выходного файла, например, combined_project.txt'
    )
    parser.add_argument(
        '--exclude',
        nargs='*',
        default=['.git', '__pycache__', 'venv', 'node_modules'],
        help='Список директорий для игнорирования (по умолчанию: .git, __pycache__, venv, node_modules)'
    )
    parser.add_argument(
        '--extensions',
        nargs='*',
        default=['.py', '.js', '.html', '.css', '.json', '.md', '.txt'],
        help='Список расширений файлов для включения (по умолчанию: .py, .js, .html, .css, .json, .md, .txt)'
    )

    # Дополнительная опция для расширенной справки
    parser.add_argument(
        '--help-extended',
        action='store_true',
        help='Вывести более подробные инструкции и примеры (extended usage)'
    )

    args = parser.parse_args()

    # Если пользователь запросил расширенную справку
    if args.help_extended:
        print_extended_help()
        sys.exit(0)

    # Если пользователь ввёл "help" вместо project_dir
    if args.project_dir == 'help' or not args.project_dir or not args.output_file:
        parser.print_help()
        print("\nПример использования: combine-project /path/to/project combined_project.txt")
        print("Более подробные примеры: combine-project --help-extended\n")
        sys.exit(0)

    # Запускаем основную логику
    combine_project(
        root_dir=args.project_dir,
        output_file=args.output_file,
        exclude_dirs=args.exclude,
        text_extensions=args.extensions
    )

def print_extended_help():
    """
    Печатает расширенную справку с примерами.
    """
    msg = r"""
Расширенная справка (Extended Help)
-----------------------------------

Скрипт объединяет все текстовые файлы (по расширениям) в заданной директории и её поддиректориях в один выходной файл.

Аргументы:
  project_dir            Путь к корневой директории проекта
  output_file            Имя выходного файла

Опции:
  --exclude              Список директорий, которые нужно пропустить
  --extensions           Список расширений текстовых файлов

Примеры:

1) Минимальный пример:
   combine-project /home/user/MyProject combined_project.txt

   В результате получится "combined_project.txt", где будут перечислены все файлы
   (по умолчанию с расширениями .py, .js, .html, .css, .json, .md, .txt).

2) Игнорируем некоторые директории и расширяем список расширений:
   combine-project . all_code.txt --exclude .git .idea --extensions .py .js .java

   Объединит все файлы с расширениями .py, .js, .java, пропуская директории .git и .idea.

3) Получить эту расширенную справку:
   combine-project --help-extended

Автор: Your Name (you@example.com)
Версия: 0.1.0
"""
    print(msg)
