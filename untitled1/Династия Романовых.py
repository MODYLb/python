n = int(input())
a = dict()

for i in range(n - 1):
    s = input().split()
    a[s[0]] = s[1]

b = dict()

values = []
for i in a.values():
    values.append(i)
keys = []
for i in a.keys():
    keys.append(i)
c = set(keys + values)

# 1 cпособ - прогонка через цикл for

for i in c:
    counter = 0
    j = i
    while j in a.keys():
        counter += 1
        j = a[j]
    b[i] = counter

for i in sorted(c):
    print(i, b[i])

# 2 cпособ - создание функции

def howmuch(i):
    counter = 0
    while i in a.keys():
        counter += 1
        i = a[i]
    b[i] = counter
    return counter

for i in sorted(c):
    print(i, howmuch(i))

# 3 способ - рекурсия

def howmuch(i):
    if i not in a.keys():
        return 0
    else:
        return 1+howmuch(a[i])

for i in sorted(c):
    print(i, howmuch(i))