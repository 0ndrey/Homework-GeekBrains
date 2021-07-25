def calcul():
    sum = 0
    a = False
    while a == False:
        number = input('Введите последовательность чисел или "z" чтобы закончить: ').split()

        result = 0
        for i in range(len(number)):
            if number[i] == 'z' or number[i] == 'Z':
                a = True
                break
            else:
                result = result + int(number[i])
        sum = sum + result
        print(f'Сумма на данный момент: {sum}')
    print(f'Конечная сумма: {sum}')


calcul()