from datetime import *

n = 100
# (1+2+...+100)^2 - (1^2 + 2^2 + ... + 100^2) = 2(1*2 + 1*3 + ... 2*1 + 2*2 + ... + 100*100)
ans = 0
x = 0
y = 0

t1 = datetime.now()
for i in range(1, n + 1):
    for j in range(i, n + 1):
        if i != j:
            ans += 2 * i * j
t2 = datetime.now()
print(ans)
print(t2 - t1)


t3 = datetime.now()
for i in range(1, n + 1):
    x += i
x **= 2
for i in range(1, n + 1):
    y += i ** 2
t4 = datetime.now()
print(x - y)
print(t4 - t3)