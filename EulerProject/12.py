treug = 0

def prist(treug):
    a = dict()
    while treug % 2 == 0:
        a[2] = a.get(2, 0) + 1
        treug //= 2
    j = 3
    while treug != 1:
        while treug % j == 0:
            a[j] = a.get(j, 0) + 1
            treug //= j
        j += 2
    answer = 1
    for j in a.values():
        answer *= j + 1
    return answer

for i in range(1, n):
    treug += i
    if prist(treug) > 500:
        print(treug)
        exit()