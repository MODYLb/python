# Поиск в глубину
# Связанный граф
M = [[False, True, False, False, False],
     [False, False, True, False, False],
     [False, False, False, True, False],
     [False, False, False, False, True],
     [False, False, False, False, False]]

colours = ['White' for i in range(len(M))]

def SearchInDeep(M, i=0):
    colours[i] = 'Grey'
    for j in range(len(M)):
        if M[i][j] == True and colours[j] == 'White':
            SearchInDeep(M, j)
    colours[i] = 'Black'

SearchInDeep(M, 0)
print(colours)

# Поиск в глубину
# Несвязанный граф

N = [[False, True, False, False, False],
     [False, False, True, False, False],
     [False, False, False, False, False],
     [False, False, False, False, True],
     [False, False, False, False, False]]

def SearchInDeep1(N, i):
    def SearchInDeep2(M, i=0):
        colours[i] = 'Grey'
        for j in range(len(M)):
            if M[i][j] == True and colours[j] == 'White':  # colours[j] == 'White' - это чтобы обойти циклы в графе
                SearchInDeep2(M, j)
        colours[i] = 'Black'
    for i in range(len(N)):
        if colours[i] == 'White':
            SearchInDeep2(N, i)

SearchInDeep1(N, 0)
print(colours)


# Понять, есть ли цикл в графе
# Связанный граф

K = [[False, True, False, False, False],
     [False, False, True, False, False],
     [True, False, False, True, False],
     [False, False, False, False, True],
     [False, False, False, False, False]]

coloursCycle = ['White' for i in range(len(K))]

Having_a_cycle = False

def SearchInDeepCycle(K, i=0):
    global Having_a_cycle
    coloursCycle[i] = 'Black'
    for j in range(len(K)):
        if K[i][j] == True and coloursCycle[j] == 'White':
            SearchInDeepCycle(K, j)
        elif K[i][j] == True and coloursCycle[j] == 'Black':
            Having_a_cycle = True
if Having_a_cycle:
    print('Есть цикл!')
else:
    print('Нету цикла!')

SearchInDeepCycle(K, 0)
print(coloursCycle)


# Понять, есть ли цикл в графе
# Несвязанный граф

L = [[False, True, False, False, False, False],
     [False, False, False, False, False, False],
     [False, False, False, True, False, False],
     [False, False, False, False, True, False],
     [False, False, False, True, False, True],
     [False, False, False, False, False, False]]

def SearchInDeepCycle1(L):
    coloursCycle1 = ['White' for i in range(len(L))]
    Having_a_cycle1 = False
    def SearchInDeepCycle2(L, i):
        nonlocal Having_a_cycle1
        coloursCycle1[i] = 'Grey'
        for j in range(len(L)):
            if L[i][j] == True and coloursCycle1[j] == 'White':
                SearchInDeepCycle2(L, j)
            elif L[i][j] == True and coloursCycle1[j] == 'Grey':
                Having_a_cycle1 = True
                break
        coloursCycle1[i] = 'Black'
    for i in range(len(L)):
        if coloursCycle1[i] == 'White':
            SearchInDeepCycle2(L, i)
            if Having_a_cycle1:
                break
    if Having_a_cycle1:
        print('Есть цикл!')
    else:
        print('Нету цикла!')
    print(coloursCycle1)

SearchInDeepCycle1(L)