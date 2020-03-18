def sum(a):
    if len(a) == 1:
        return a[0]
    else:
        return a.pop(0) + sum(a)

a = [2,4,9,87,5656]
summa = 0

for i in a:
    summa += i

print(sum(a))
print(summa)