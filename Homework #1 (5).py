plus = float(input("Выручка:"))
minus = float(input("Издержки:"))

rent = (plus - minus) / plus

if plus > minus:
    print("Финансовый результат: фирма приносит прибыль")
    print("Рентабельность выручки: ", rent)
    n = int(input("Введите количество сотрудников фирмы:"))
    m = (plus - minus) / n
    print("Прибыль фирмы в расчете на одного сотрудника:", m)
elif plus == minus:
    print("Финансовый результат: фирма работает в ноль")

else:
    print("Финансовый результат: фирма работает в убыток")