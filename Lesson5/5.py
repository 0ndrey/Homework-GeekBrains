import random

with open('Text5.txt', 'w') as file:
    for i in range(10):
        file.write(f'{random.randint(1, 7)} ')

with open('Text5.txt', '+r') as file:

    def summary():
        my_numb = file.read().split()
        print(sum(map(int, my_numb)))
    summary()

