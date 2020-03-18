a = []
with open('18.txt') as f:
    for i in f:
        a.append([int(i) for i in i.split()])

def maxway(a, i):
    if i == 0:
        return a[i]
    else:
        f = maxway(a, i - 1)
        return [a[i][0] + f[0]] + [a[i][j] + max(f[j], f[j-1]) for j in range(1, i)] + [a[i][i] + f[i - 1]]

print(max(maxway(a, len(a) - 1)))