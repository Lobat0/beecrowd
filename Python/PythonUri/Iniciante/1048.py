sal = float(input())
if sal <= 400:
    perce = 15
elif 400 < sal <= 800:
    perce = 12
elif 800 < sal <= 1200:
    perce = 10
elif 1200 < sal <= 2000:
    perce = 7
else:
    perce = 4
reajuste = (sal * perce) / 100
print('Novo salario: {:.2f}'.format(sal + reajuste))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(perce))
