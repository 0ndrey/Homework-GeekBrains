a = float(input("Результат в 1 день:"))
b = float(input("Желаемый результат:"))

n = 1
while a < b:
    a = a + 0.1 * a
    n += 1
    if a >= b:
        print(f"на {n} день спортсмен достиг нужного результата")
        break
    else:
        continue

