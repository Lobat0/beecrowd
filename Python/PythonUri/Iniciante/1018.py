N = int(input(''))
n1 = N // 100
n2 = (N - (n1*100)) // 50
n3 = (N - (n1*100) - (n2*50)) // 20
n4 = (N - (n1*100) - (n2*50) - (n3*20)) // 10
n5 = (N - (n1*100) - (n2*50) - (n3*20) - (n4*10)) // 5
n6 = (N - (n1*100) - (n2*50) - (n3*20) - (n4*10) - (n5*5)) // 2
n7 = (N - (n1*100) - (n2*50) - (n3*20) - (n4*10) - (n5*5) - (n6*2)) // 1

print('{}'.format(N))
print('{} nota(s) de R$ 100,00'.format(n1))
print('{} nota(s) de R$ 50,00'.format(n2))
print('{} nota(s) de R$ 20,00'.format(n3))
print('{} nota(s) de R$ 10,00'.format(n4))
print('{} nota(s) de R$ 5,00'.format(n5))
print('{} nota(s) de R$ 2,00'.format(n6))
print('{} nota(s) de R$ 1,00'.format(n7))