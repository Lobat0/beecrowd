a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

x = (b * b) - (4 * a * c)
if a == 0 or x < 0:
    print('Impossivel calcular')
else:
    r1 = (-b + (x**(1/2))) / (2 * a)
    r2 = (-b - (x**(1/2))) / (2 * a)
    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5f}'.format(r2))
