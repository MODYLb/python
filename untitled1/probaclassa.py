class Zalupa:
    count = 0
    def __init__(self, name, age = 22):
        self.name = name
        self.age = age
        Zalupa.count += 1

    def __str__(self):
        return f'class = {self.__class__.__name__}, ' + ', '.join([f'{i} = {j}' for i, j in self.__dict__.items()])

    def __add__(self, other):   # For x
        return Zalupa(self.name + other)    # если просто self.name + other - выведется Yarik pizdat, c __radd__ аналогично

    def __radd__(self, other):  # for y
        return Zalupa(other + self.name)

    # def setdata(self, name, age = 22):   # For K
    #     self.name = name
    #     self.age = age
    #
    # def display(self):   # For K
    #     print(self.__class__.__name__, self.name)



class Pipka(Zalupa):
    def display(self):
        #print(f'Current value = "%s"' % self.name)
        print('Current value = {}'.format(self.name))


class Looser:
    def __init__(self, name, age):
        self.c = Zalupa(self, name, age = 33)

if __name__ == '__main__':
    I = Zalupa('Yarik', 54)
    print(I)
    print(Zalupa.count)

    x = I + ' pizdat'
    y = 'pizdat ' + I
    print(x)
    print(y)
    print(x.name)

    # K = Zalupa()
    # Zalupa.setdata(K, 'wow')
    # K.display()

    L = Looser('Max')
    print(L.c)


