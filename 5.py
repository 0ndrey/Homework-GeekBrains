my_list = [7, 5, 3, 3, 2]
a = int(input('Введите новый элемент'))
for num, el in enumerate(my_list):
    if a > el:
        my_list.insert(num, a)
        break
else:
    my_list.append(a)

print(my_list)