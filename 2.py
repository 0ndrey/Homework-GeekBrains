a = input('enter name')
b = input('enter surname')
c = int(input('enter year'))
d = input('enter city')
e = input('enter email')


def data(**kwargs):
    print(kwargs)


data(name=a, surname=b, year=c, city=d, email=e)
