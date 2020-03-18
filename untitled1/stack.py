class Stack:

    def __init__(self, *a):
        self.__xyi = list(a)

    def pokazlast(self):
        return self.__xyi[-1]

    def add(self, *b):
        self.__xyi += list(b)

    def pop(self):
        return self.__xyi.pop()

I = Stack(1, 2, 3)
I.add(4, 5)

print(I.pop())

