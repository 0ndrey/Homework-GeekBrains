list1 = (input("Введите количество элементов списка "))
list2 = list1.split()

for i in range(int(len(list2)/2)):
        list2[i], list2[i + 1] = list2[i + 1], list2[i]

print(list2)