el_count = int(input("Введите количество элементов списка "))
list1 = []
num = 0
a = 0
while num < el_count:
    list1.append(input("Введите значение "))
    num += 1

for el in range(int(len(list1)/2)):
        list1[a], list1[a + 1] = list1 [a + 1], list1[a]
        a += 2

print(list1)