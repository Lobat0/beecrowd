valores = []
ordem = []
v1, v2, v3 = input().split()
v1 = int(v1)
v2 = int(v2)
v3 = int(v3)
valores.append(v1)
valores.append(v2)
valores.append(v3)
ordem = valores[:]
ordem.sort()

for i in ordem:
    print(i)

print()

for c in valores:
    print(c)
