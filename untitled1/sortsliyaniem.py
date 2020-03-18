def merge(A, B):
    C = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    C += A[i:] + B[j:]
    return C

def merge_sort(isx):
    if len(isx) <= 1:
        return isx
    middle = len(isx) // 2
    return merge(merge_sort(isx[:middle]), merge_sort(isx[middle:]))

isx = [2, 3, 8, 6, 7, 1]
print(merge_sort(isx))