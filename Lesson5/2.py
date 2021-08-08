with open('text2.txt') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        counter = len(line.split())
        print(f'#{i+1} - {counter}')