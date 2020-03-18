def left_bound(s:list, a):
    left = -1
    right = len(s)
    while right - left > 1:
        middle = (right + left) // 2
        if s[middle] < a:
            left = middle
        else:
            right = middle
    return left

def right_bound(s:list, a):
    left = -1
    right = len(s)
    while right - left > 1:
        middle = (right + left) // 2
        if s[middle] <= a:
            left = middle
        else:
            right = middle
    return right

def full_bin_search(s:list, a):
    left_b = left_bound(s, a)
    right_b = right_bound(s, a)
    if right_b - left_b == 1:
        return left_b, right_b
    elif right_b - left_b == 2:
        return left_b + 1
    else:
        return left_b + 1, right_b - 1

s = [1, 2, 3, 4, 4, 4, 6]

print(full_bin_search(s, 5))