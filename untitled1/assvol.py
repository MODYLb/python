class Simple:
    count = 0

    def __init__(self, name, age, job='None', salary=0):
        self.name = name
        self.age = age
        self.job = job
        self.salary = salary
        Simple.count += 1

    def __del__(self):
        Simple.count -= 1

    def __str__(self):
        return f'class: {self.__class__.__name__}, ' + ', '.join([f'{i} = {j}' for i, j in self.__dict__.items()])
        # return f'class: {self.__class__.__name__}, name = {self.name}, age = {self.age}'

    @staticmethod
    def howmany():
        print(Simple.count)

    def __setattr__(self, key, value):
        if __name__ != '__main__':        # if key in self.__dict__.keys(): - позволяет сделать так, чтоб никто (даже я) не менял ниче
            print('Not today')            # pass
        else:                             # if key in [age, job] - так можно сделать, чтоб нельзя было менять конкретные атрибуты
            self.__dict__[key] = value

    def upsalary(self, up=30):
        self.salary *= 1 + up/100
        self.salary = round(self.salary, 2)   # Округлил до 2 знаков


class Developer:   # Делегирование
    def __init__(self, name, age, salary=0):
        self.cap = Simple(name, age, job='Developer', salary=salary)

    def __str__(self):
        return str(self.cap)

    def __getattr__(self, item):
        return getattr(self.cap, item)

    def upsalary(self, up=30, bonus=10):
        self.cap.upsalary(up + bonus)


class Ofik(Simple):
    def __init__(self, name, age, salary=0, rang='Youngster'):
        Simple.__init__(self, name, age, job='Ofik', salary=salary)
        self.rang = rang

    def upsalary(self, up=30, bonus=3):
        Simple.upsalary(self, up + bonus)


class Firma:
    def __init__(self, name, *a):
        self.name = name
        self.spisok = list(a)

    def printall(self):
        for i in self:        # for i in self.spisok:  <--- до перегрузки оператора __getitem__
            print(i)

    def __getitem__(self, item):   # a[item]
        return self.spisok[item]

    def addsub(self, *b):
        self.spisok += list(b)

import shelve    # позволяет хранить объекты по ключам

if __name__ == '__main__':    # Тестировщик
    I1 = Simple('Yarik', 22, 'Student')
    I2 = Simple('Sanya', 54, 'Developer', 300000)
    I2.upsalary()
    Simple.howmany()
    # print(I1)
    # print(I2)
    #
    I3 = Developer('Max', 17, 10000)
    # print(I3.salary)
    # I3.upsalary()
    # print(I3.salary)
    #
    I4 = Ofik('Yurik', 13, 40000)
    # print(I4)
    # I4.upsalary()
    # print(I4.salary)
    #
    # for i in [I1, I2, I3, I4]:
    #     i.upsalary(up=10)
    #     print(i.salary)

    # a = Firma('Uzniki', I1, I2, I3)
    # print(*a.spisok, sep='\n')
    # a.printall()
    # print(a.spisok[0])
    # print(*a[2:])
    # a.printall()

    # a.addsub(I4)
    # print(*a)
    # print(*a.spisok, sep='\n')

    db = shelve.open('db')
    db[I2.name] = I2
    print(db['Sanya'])
    db.close()