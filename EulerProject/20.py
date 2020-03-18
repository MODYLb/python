from math import factorial
number = 0

a = str(factorial(100))
for i in range(len(a)):
    number += int(a[i])

print(number)