dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('Text4.txt', 'r') as file, open('new_Text4.txt', 'w') as new_file:
    lines = file.readlines()
    for line in lines:
        spliter = line.split()
        rus = dict.get(spliter[0])
        new_file.write(line.replace(spliter[0], rus))
