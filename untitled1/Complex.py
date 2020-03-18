class Complex:
    def __init__(self, x, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        if self.y == 0:
            return f'{self.x}'
        elif self.y < 0:
            return f'{self.x} - {-self.y}i'
        else:
            return f'{self.x} + {self.y}i'

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.x + other.x, self.y + other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(self.x + other, self.y)
        else:
            raise TypeError

    def __radd__(self, other):
        # if isinstance(other, Complex):
        #     return Complex(self.x + other.x, self.y + other.y)
        # elif isinstance(other, int) or isinstance(other, float):
        #     return Complex(self.x + other, self.y)
        # else:
        #     raise TypeError
        return Complex.__add__(self, other)

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.x - other.x, self.y - other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(self.x - other, self.y)
        else:
            raise TypeError

    def __rsub__(self, other):
        if isinstance(other, Complex):
            return Complex(other.x - self.x, other.y - self.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(other - self.x, self.y)
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.x * other.x - self.y * other.y, self.y * other.x + self.x * other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(self.x * other, self.y * other)
        else:
            raise TypeError

    def __rmul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.x * other.x - self.y * other.y, self.y * other.x + self.x * other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(self.x * other, self.y * other)
        else:
            raise TypeError
        # return Complex.__mul__(self, other) - или так

    def __eq__(self, other):
        if isinstance(other, Complex):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, int) or isinstance(other, float):
            return self.x == other
        else:
            raise TypeError

    def obr(self):
        return Complex(self.x / (self.x ** 2 + self.y ** 2), -self.y / (self.x ** 2 + self.y ** 2))

    def __truediv__(self, other):
        if isinstance(other, Complex):
            return Complex(self * other.obr())
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(self.x / other, self.y / other)
        else:
            raise TypeError

    def __rtruediv__(self, other):
        if isinstance(other, Complex):
            return Complex(self * other.obr())
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(other / self.x, other / self.y)
        else:
            raise TypeError

if __name__ == '__main__':
    I1 = Complex(2, 1)
    I2 = Complex(2, 1)
    I3 = Complex(2, 0)
    I1.obr()
    print(I1.obr() * I1)

