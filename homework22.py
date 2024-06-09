#     Создайте переменную с этим файлом
#     Распечатайте содержимое текстового файла в консоль, используя оператор with
#
# Чем отличается использование оператора with open(file_name...) от простого использования file.close()?

file_name = 'Text.txt'
with open(file_name, mode='r') as file:
    for line in file:
        print(line, end='')

# with - автоматически закрывает файл
