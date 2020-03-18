import random

a = [9, 7, 5, 98, 5, 5]

def bistrsorthaara(a):
    if len(a) == 0:
        return a
    else:
        imid = random.randint(0, len(a) - 1)
        mid = a[imid]
        less = [i for i in a[:imid] + a[(imid+1):] if a[imid] >= i]
        more = [i for i in a[:imid] + a[(imid+1):] if a[imid] < i]
        return bistrsorthaara(less) + [mid] + bistrsorthaara(more)

def full_bistrsorthaara(a):
    if len(a) <= 1:
        return a
    else:
        imid = random.randint(0, len(a) - 1)
        mid = a[imid]
        less = [i for i in a if a[imid] > i]
        mid = [i for i in a if a[imid] == i]
        more = [i for i in a if a[imid] < i]
        return bistrsorthaara(less) + mid + bistrsorthaara(more)

print(bistrsorthaara(a))
print(full_bistrsorthaara(a))