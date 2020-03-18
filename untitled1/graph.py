# Задача выводит, является граф Эйлеровым или нет, исходя из правила, что граф является Эйлеровым, если степени всех его вершин кратны 2
# Можно сделать с помощью Counter

M = [[False, True, False, False, False],
     [True, False, True, False, False],
     [False, True, False, True, False],
     [False, False, True, False, True],
     [False, False, False, True, False]]

def EulerGraph(M):
    a = len(M)
    for i in range(a):
        num = 0
        for j in range(a):
            if M[i][j]:   # == True
                num += 1
        if num != 0 and num % 2 != 0:
            return False
    return True

print(EulerGraph(M))