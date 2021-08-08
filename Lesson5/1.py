file_obj = open('Text.txt', 'w')
line = input(f'Введите текст:\n')
while line:
    file_obj.writelines(line)
    line = input('Введите текст:\n')
file_obj.close()