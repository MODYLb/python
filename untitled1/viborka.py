import random

a = [random.randint(0, 10) for i in range(9)]
print(a)

def viborka(a):
    for i in range(len(a) - 1):
        imin = min(range(i, len(a)), key=a.__getitem__)
        a[imin], a[i] = a[i], a[imin]
    return a


print(viborka(a))