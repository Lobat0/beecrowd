a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
cont = 0
if b - c < a < b + c:
    cont += 1
if a - c < b < a + c:
    cont += 1
if a - b < c < a + b:
    cont += 1
if cont == 3:
    print('Perimetro = {}'.format(a + b + c))
else:
    print('Area = {}'.format(((a + b) * c)/2))
