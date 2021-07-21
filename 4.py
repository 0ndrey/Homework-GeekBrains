my_str = input("введите строку ")
word = []
num = 1
for el in range(my_str.count(' ') + 1):
    word = my_str.split()
    if len(str(word)) <= 10:
        print(f" {num} {word [el]}")
        num += 1
    else:
        print(f" {num} {word [el] [0:10]}")
        num += 1