from Sito import *

def mnoj(n):

    a = dict()
    b = sito(n)
    c = sorted([i for i in b])

    i = 0
    isx = n   # для печати в конце

    while n != 1:                #for i in c:
        while n % c[i] == 0:     #n % i == 0
            n /= c[i]
            a[c[i]] = a.get(c[i], 0) + 1
        i += 1

    spis=[]
    for i, j in a.items():
        x = f'{i}^{j}'
        spis.append(x)

    return a        #вывод словаря


#print(mnoj(76))