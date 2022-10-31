contdd = conthh = contmm = contss = 0

ddini = input().split('Dia ')
ddini = ddini[1]
ddini = int(ddini)
hhini, mmini, ssini = input().split(' : ')
hhini = int(hhini)
mmini = int(mmini)
ssini = int(ssini)


ddfin = input().split('Dia ')
ddfin = ddfin[1]
ddfin = int(ddfin)
hhfin, mmfin, ssfin = input().split(' : ')
hhfin = int(hhfin)
mmfin = int(mmfin)
ssfin = int(ssfin)

while True:
    if ddini == ddfin and hhini == hhfin and mmini == mmfin and ssini == ssfin:
        break
    contss += 1
    ssini += 1
    if ssini == 60:
        ssini = 0
        mmini += 1
    if mmini == 60:
        mmini = 0
        hhini += 1
    if hhini == 24:
        hhini = 0
        ddini += 1

    if contss == 60:
        contss = 0
        contmm += 1
    if contmm == 60:
        contmm = 0
        conthh += 1
    if conthh == 24:
        conthh = 0
        contdd += 1

print('{} dia(s)'.format(contdd))
print('{} hora(s)'.format(conthh))
print('{} minuto(s)'.format(contmm))
print('{} segundo(s)'.format(contss))
