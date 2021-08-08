class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, mass_per_m, depth):

        return self._length * self._width * mass_per_m * depth/1000


road = Road(20, 5000)
print(f'Масса покрытия: {road.mass(25, 5)} тонн')