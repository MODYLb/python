a = []
Max = 0

with open('18.txt') as f:
    for i in f:
        a.append([int(i) for i in i.split()])

for i in range(2 ** (len(a)-1)):
    k = 0
    sum = a[0][k]
    way = bin(i)[2:].rjust(len(a) - 1, '0')
    for j in range(len(a) - 1):
        if way[j] == '1':
            k += 1
        sum += a[j + 1][k]
    Max = max(Max, sum)

print(Max)