import os
import time

#Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
# Примените os.path.join для формирования полного пути к файлам.
# Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# Используйте os.path.getsize для получения размера файла.
# Используйте os.path.dirname для получения родительской директории файла.
directory = '.'
for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(root,file)
    filetime = os.path.getmtime(file)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(file)
    parent_dir = os.path.dirname(os.getcwd())
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')