def my_func(*args):
    x = abs(float(input("Введите действительное положительное число")))
    y = int(input("Введите целое отрицательное число"))
    return x**y


print(my_func())