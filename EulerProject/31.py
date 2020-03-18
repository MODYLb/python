a = sorted([1, 2, 5, 10, 20, 50, 100, 200])
N = 200

def xz(a, N):
    if N == 0 or len(a) == 1:
        return 1
    elif a[-1] > N:
        return xz(a[:-1], N)
    else:
        return xz(a[:-1], N) + xz(a, N - a[-1])

print(xz(a, N))