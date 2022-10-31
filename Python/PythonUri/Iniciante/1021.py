'''N = float(input(''))
#notas
n1 = int(N // 100)
n2 = int((N - (n1*100)) // 50)
n3 = int((N - (n1*100) - (n2*50)) // 20)
n4 = int((N - (n1*100) - (n2*50) - (n3*20)) // 10)
n5 = int((N - (n1*100) - (n2*50) - (n3*20) - (n4*10)) // 5)
n6 = int((N - (n1*100) - (n2*50) - (n3*20) - (n4*10) - (n5*5)) // 2)
#moedas
n7 = int((N - (n1*100) - (n2*50) - (n3*20) - (n4*10) - (n5*5) - (n6*2)) // 1)
n8 = int((N - (n1*100) - (n2*50) - (n3*20) - (n4*10) - (n5*5) - (n6*2) - (n7*1)) // 0.5)
n9 = int((N - (n1*100) - (n2*50) - (n3*20) - (n4*10) - (n5*5) - (n6*2) - (n7*1) - (n8*0.5)) // 0.25)
n10 = int((N - (n1*100) - (n2*50) - (n3*20) - (n4*10) - (n5*5) - (n6*2) - (n7*1) - (n8*0.5) - (n9*0.25)) // 0.10)
n11 = int((N - (n1*100) - (n2*50) - (n3*20) - (n4*10) - (n5*5) - (n6*2) - (n7*1) - (n8*0.5) - (n9*0.25) - (n10*0.10)) // 0.05)
n12 = int((N - (n1*100) - (n2*50) - (n3*20) - (n4*10) - (n5*5) - (n6*2) - (n7*1) - (n8*0.5) - (n9*0.25) - (n10*0.10) - (n11*0.05)) // 0.01)
print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(n1))
print('{} nota(s) de R$ 50.00'.format(n2))
print('{} nota(s) de R$ 20.00'.format(n3))
print('{} nota(s) de R$ 10.00'.format(n4))
print('{} nota(s) de R$ 5.00'.format(n5))
print('{} nota(s) de R$ 2.00'.format(n6))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(n7))
print('{} moeda(s) de R$ 0.50'.format(n8))
print('{} moeda(s) de R$ 0.25'.format(n9))
print('{} moeda(s) de R$ 0.10'.format(n10))
print('{} moeda(s) de R$ 0.05'.format(n11))
print('{} moeda(s) de R$ 0.01'.format(n12))'''

valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    quantidade_nota = int(valor / nota)
    print('{} nota(s) de R$ {:.2f}'.format(quantidade_nota, nota))
    valor -= quantidade_nota * nota

print('MOEDAS:')
for moeda in moedas:
    quantidade_moeda = int(round(valor, 2) / moeda)
    print('{} moeda(s) de R$ {:.2f}'.format(quantidade_moeda, moeda))
    valor -= quantidade_moeda * moeda