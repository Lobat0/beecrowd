inicial, final = input().split()
inicial = int(inicial)
final = int(final)
tempo = []
temp = inicial
cont = reserva = 0
for c in range(0, 24):
    tempo.append(c)
if inicial == final:
    print('O JOGO DUROU 24 HORA(S)')
else:
    while True:
        temp += 1
        cont += 1
        if temp == 24:
            temp = 0
        if tempo[final] == tempo[temp]:
            break
    print('O JOGO DUROU {} HORA(S)'.format(cont))
