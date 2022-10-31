#a = float(input())
#b = float(input())
#c = float(input())
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
triangulo = (a * c)/2
circulo = (c**2) * 3.14159
trapezio = ((a + b) * c)/2
quadrado = b * b
retangulo = a * b
print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))