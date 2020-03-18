from datetime import *

from math import sqrt

# n = int(10**7)

# def prost(n):
#     if n == 2:
#         return True
#     elif n == 0 or n == 1 or n % 2 == 0:
#         return False
#     else:
#         for i in range(3, int(sqrt(n)) + 1, 2):
#             if n % i == 0:
#                 return False
#         return True

# t1 = datetime.now()
# a = set(i for i in range(n) if prost(i))
# t2 = datetime.now()
# print(a)
# print(t2 - t1)

n = int(10 ** 7)

t1 = datetime.now()

def sito(n):
    a = (set(range(3, n+1, 2))) | {2}
    for p in range(3, int(sqrt(n)), 2):
        d_e = p ** 2
        while d_e <= n:
            a.discard(d_e)
            d_e += 2*p
    return a

t2 = datetime.now()

if __name__ == '__main__': # Это хуйня, чтоб если мы Сито запустили здесь, то оно распечаталось, а если в импортированной,
    print(sito(n))         # то принта не будет
    print(t2 - t1)

# if any(not prost(i) for i in a):   Проверка
#     print('есть косяк')
# else:
#     print('все найс')


