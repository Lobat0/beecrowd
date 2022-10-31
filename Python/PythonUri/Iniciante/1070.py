n = int(input())
i = n+13
count = 0
for c in range(n, i):
    if c % 2 == 1:
        count += 1
        if count <= 6:
            print(c)
