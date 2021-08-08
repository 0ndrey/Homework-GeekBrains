class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start')


class Pen(Stationary):
    def draw(self):
        print(f'You took {self.title}. Start with {self.title}')


class Pencil(Stationary):
    def draw(self):
        print(f'You took {self.title}. Start with {self.title}')


class Handle(Stationary):
    def draw(self):
        print(f'You took {self.title}. Start with {self.title}')


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
pen.draw()
pencil.draw()
handle.draw()
