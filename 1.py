
def div_func (*args):
    arg1 = float(input("Введите 1 число"))
    arg2 = float(input("Введите 2 число"))
    if arg2 != 0:
      return arg1 / arg2
    else:
       print ('Второе число не должно быть 0')



print("Результат:", div_func())

