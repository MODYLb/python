import random

a = [random.randint(0, 10) for i in range(9)]
print(a)
x = True

while x:
    x = False
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            x = True

print(a)