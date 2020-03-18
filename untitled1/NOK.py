from ProstieMnojiteliForNOK import *

n = 10
a = dict()

keys = []
values = []

new = dict()

# for i in range(2, n+1):
#     a = mnoj(i)
#     for j, k in a.items():
#         if j not in new.keys():
#             new[j] = k
#         elif j in new.keys() and int(k) > int(new[j]):
#             new[j] = k

for i in range(2, n+1):
    for j, k in mnoj(i).items():
        new[j] = max(new.get(j,0), k)

x = 1
for i, j in new.items():
    x *= i ** j

print(x)