my_str = input("введите строку ")
word = my_str.split()
for num, word in enumerate(word):
        print(f" {num} {word[0:10]}")
