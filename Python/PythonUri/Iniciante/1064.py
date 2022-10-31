lista = []
media = 0
positivo = 0


for c in range(0, 6):
    num = float(input())
    lista.append(num)

for i in lista:
    if i > 0:
        positivo += 1
        media += i

print('{} valores positivos'.format(positivo))
print('{:.1f}'.format(media/positivo))
