def my_funk(*args):
    arg1 = float(input("Введите 1 число"))
    arg2 = float(input("Введите 2 число"))
    arg3 = float(input("Введите 3 число"))
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


print("Результат:", my_funk())


# Можно ли с помощью какой-либо команды укоротить код и избежать цикла?
