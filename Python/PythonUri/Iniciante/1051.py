sal = float(input())
imp = 0
if sal <= 2000:
    print('Isento')
elif sal <= 3000:
    imp = (sal - 2000) * 0.08
elif sal <= 4500:
    imp = (sal - 3000) * 0.18 + (1000 * 0.08)
else:
    imp = (sal - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
if imp != 0:
    print('R$ {:.2f}'.format(imp))
