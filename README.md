# combine_project

---

## Оглавление (Table of Contents)

1. [Описание (RU)](#описание-ru)  
2. [Установка и использование (RU)](#установка-и-использование-ru)  
3. [Примеры (RU)](#примеры-ru)  
4. [Description (EN)](#description-en)  
5. [Installation and Usage (EN)](#installation-and-usage-en)  
6. [Examples (EN)](#examples-en)  

---

## Описание (RU)

**combine_project** — это утилита, которая рекурсивно сканирует заданную директорию и собирает все текстовые файлы (по расширениям), записывая их содержимое в единый выходной файл. Для каждого файла в результирующем файле добавляются заголовки, указывающие относительный путь к исходному файлу.

### Возможности

- Рекурсивный обход каталога.
- Игнорирование определённых директорий (например, `.git`, `venv`, `node_modules`).
- Гибкая настройка расширений текстовых файлов (`.py`, `.js`, `.html` и т.д.).
- Выдача расширенной справки по флагу `--help-extended`.

---

## Установка и использование (RU)

### 1. Установка через виртуальное окружение

```bash
cd /путь/к/combine_project
python3 -m venv venv
source venv/bin/activate
pip install .
```

После этого команда `combine-project` станет доступна в вашем активированном виртуальном окружении.

### 2. Установка через pipx (рекомендуется для CLI-инструментов)

```bash
pipx install /путь/к/combine_project
```

(Не забудьте установить `pipx`, если он отсутствует, выполнив что-то вроде `sudo apt install pipx` или используя инструкции для вашего дистрибутива.)

### 3. Запуск

После установки (в виртуальное окружение или через `pipx`):

```bash
combine-project /путь/к/проекту combined_output.txt
```

Опции:

- `--exclude`: директории, которые нужно пропустить.  
- `--extensions`: расширения текстовых файлов.  
- `--help-extended`: расширенная справка.

---

## Примеры (RU)

1. **Минимальный пример**:

```bash
combine-project /home/user/MyProject combined_project.txt
```

Будет создан файл `combined_project.txt` со всем кодом из файлов `.py`, `.js`, `.html`, `.css`, `.json`, `.md`, `.txt`.

2. **Исключаем некоторые папки**:

```bash
combine-project /home/user/MyProject all_code.txt --exclude .git .idea venv
```

Выходной файл `all_code.txt` не будет содержать файлы из `.git`, `.idea`, `venv`.

3. **Расширяем список расширений**:

```bash
combine-project /home/user/JavaProject combined_java.txt --extensions .java .txt
```

В результирующий файл попадут только `.java` и `.txt` файлы.

4. **Более подробная справка**:

```bash
combine-project --help-extended
```

---

## Description (EN)

**combine_project** is a command-line utility that recursively scans the specified directory and gathers all text files (by file extension), writing their content into a single output file. For each file, a header line is added to indicate the relative path of the source file.

### Features

- Recursive directory traversal.
- Customizable exclusion of certain directories (e.g., `.git`, `venv`, `node_modules`).
- Flexible list of recognized text file extensions (`.py`, `.js`, `.html`, etc.).
- Extended help available via `--help-extended`.

---

## Installation and Usage (EN)

### 1. Virtual Environment Installation

```bash
cd /path/to/combine_project
python3 -m venv venv
source venv/bin/activate
pip install .
```

After that, the command `combine-project` will be available in your activated virtual environment.

### 2. Using pipx (Recommended for CLI Tools)

```bash
pipx install /path/to/combine_project
```

(Make sure `pipx` is installed first; e.g., `sudo apt install pipx` on Debian/Ubuntu.)

### 3. Running the Utility

Once installed (either in a venv or via pipx):

```bash
combine-project /path/to/your/project combined_output.txt
```

Options:

- `--exclude`: directories to skip.  
- `--extensions`: file extensions considered as text.  
- `--help-extended`: display extended usage instructions.

---

## Examples (EN)

1. **Minimal Example**:

```bash
combine-project /home/user/MyProject combined_project.txt
```

Creates `combined_project.txt` with content from files matching the default extensions: `.py`, `.js`, `.html`, `.css`, `.json`, `.md`, `.txt`.

2. **Exclude Some Folders**:

```bash
combine-project /home/user/MyProject all_code.txt --exclude .git .idea venv
```

The resulting `all_code.txt` will not contain files from `.git`, `.idea`, or `venv`.

3. **Extend File Extensions**:

```bash
combine-project /home/user/JavaProject combined_java.txt --extensions .java .txt
```

Only `.java` and `.txt` files will be included.

4. **Extended Help**:

```bash
combine-project --help-extended
```

---