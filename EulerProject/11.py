a = []
b = []
with open('11.txt') as f:
    for i in f:
        a.append([int(i) for i in i.split()])

Max = 0
i = 0
j = 0

for j in range(len(a)):      # столбцы
    for i in range(len(a) - 3):
        Max = max(Max, a[i][j] * a[i + 1][j] * a[i + 2][j] * a[i + 3][j])

for i in range(len(a)):     # строки
    for j in range(len(a) - 3):
        Max = max(Max, a[i][j] * a[i][j + 1] * a[i][j + 2] * a[i][j + 3])

for i in range(len(a) - 3):      # главные диагонали
    for j in range(len(a) - 3):
        Max = max(Max, a[i][j] * a[i + 1][j + 1] * a[i + 2][j + 2] * a[i + 3][j + 3])

for i in range(len(a) - 3):      # побочные диагонали
    for j in range(len(a) - 3):
        Max = max(Max, a[i + 3][j] * a[i + 2][j + 1] * a[i + 1][j + 2] * a[i][j + 3])

print(Max)