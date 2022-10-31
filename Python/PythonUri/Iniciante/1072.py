n = int(input())
dentro = fora = 0
for c in range(0, n):
    num = int(input())
    if num >= 10 and num <= 20:
        dentro += 1
    else:
        fora += 1
print(f'{dentro} in\n{fora} out')
