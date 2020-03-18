a = 1
b = 2
sum = 0
i = 0

while a <= 4000000 or b <= 4000000:
    a, b = b, a + b
    if a % 2 == 0:
        sum += a

print(sum)