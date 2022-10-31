n1 = int(input())
ano = n1 // 365
mes = (n1 - (ano * 365)) // 30
dia = (n1 - (ano * 365) - (mes * 30))
print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))
