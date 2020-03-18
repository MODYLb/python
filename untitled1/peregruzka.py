class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)

    def __add__(self, other):
        return Number(self.data + other)

    def __str__(self):
        return f'{self.data}'

X = Number(5)
Y = X - 2
Z = X + '5'
ZZ = Number.__add__(X, 5)
X += 52
print(Y)
print(Z)
print(ZZ)
print(X)