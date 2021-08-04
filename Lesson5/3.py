with open('text3.txt') as file:
    salary = []
    poor = []
    my_list = file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            poor.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(float, salary)) / len(salary)}')