with open('4tenie') as f:
    a = ''
    Max = 0
    for line in f:
        a += line.rstrip()
    for i in range(len(a)-12):
        b = 1
        for k in a[i:i+13]:
            b *= int(k)
        Max = max(Max, b)
    print(Max)
