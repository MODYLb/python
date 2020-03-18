max = 0

for i in range(999, 100, -1):
    for j in range(i, 100, -1):   # первоначально range(999, 100, -1), но мы уменьшим выбор чисел в 2 раза таким образом
        a = str(i * j)
        if a == a[::-1] and max < i * j:
            max = i * j
            imax = i
            jmax = j
print(f'{max} = {imax} * {jmax}')
