from Sito import *

def prostmnoj(n):
    a = dict()
    b = sito(n)
    c = sorted([i for i in b])
    i = 0

    while n != 1:                #for i in c:
        while n % c[i] == 0:     #n % i == 0
            n /= c[i]
            a[c[i]] = a.get(c[i], 0) + 1
        i += 1

    return a

if __name__ == '__main__':
    print(prostmnoj(54))
