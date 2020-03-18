a = [1, 2, 3, 5, 6, 8, 9, 54, 68]
x = 69

def binpoi(x, a):

    left = 0
    right = len(a)
    middle = (left + right) // 2

    while left != right:
        if x == a[middle]:
            return middle
            break
        elif x > a[middle]:
            left = middle + 1
            middle = (left + right) // 2
        else:
            right = middle
            middle = (left + right) // 2
    else:
        return 'Такого элемента нет'

print(binpoi(68, a))