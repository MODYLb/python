from datetime import *

n = 5
a = [[0 for i in range(n)] for i in range(n)]
pov = []
#a = "\n".join([" ".join(["0" for x in range(4)]) for x in range(4)])
x = 0
y = 1
k = 1
zz = 3

t1 = datetime.now()

while y <= n ** 2:
    pov.append(y)
    if y == n ** 2:
        break
    y += n - k
    if len(pov) == zz:
        k += 1
        zz += 2

j = 0
k = -1
count = 0
for i in range(1, n ** 2 + 1):
    if i >= pov[0 + count] and i <= pov[1 + count]:
        k += 1
        a[j][k] = i
    elif i > pov[1 + count] and i <= pov[2 + count]:
        j += 1
        a[j][k] = i
    elif i > pov[2 + count] and i <= pov[3 + count]:
        k -= 1
        a[j][k] = i
    elif i > pov[3 + count] and i <= pov[4 + count]:
        j -= 1
        a[j][k] = i
        if i == pov[4 + count]:
            count += 4

t2 = datetime.now()

for i in a:
    print(''.join([str(j).ljust(4) for j in i]))
print(t2 - t1)