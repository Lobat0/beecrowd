positivos = 0
for c in range(0, 6):
    num = float(input())
    if num > 0:
        positivos += 1
print('{} valores positivos'.format(positivos))
