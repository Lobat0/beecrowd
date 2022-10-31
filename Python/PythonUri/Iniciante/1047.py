hrinicial, mininicial, hrfinal, minfinal = input().split()
hrinicial = int(hrinicial)
mininicial = int(mininicial)
hrfinal = int(hrfinal)
minfinal = int(minfinal)
conthr = contmin = 0
hora = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
minuto = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
"""for c in range(0, 24):
    hora.append(c)
for c in range(0, 60):
    minuto.append(c)
print(minuto)"""
if hrinicial == hrfinal and mininicial == minfinal:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    while True:
        if hora[hrfinal] == hora[hrinicial] and minuto[minfinal] == minuto[mininicial]:
            break
        mininicial += 1
        contmin += 1
        if contmin == 60:
            contmin = 0
            conthr += 1
        if mininicial == 60:
            mininicial = 0
            hrinicial += 1
        if hrinicial == 24:
            hrinicial = 0

    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(conthr, contmin))

