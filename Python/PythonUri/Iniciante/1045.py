a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
ordem = [a, b, c]
ordem.sort(reverse=True)
a = ordem[0]
b = ordem[1]
c = ordem[2]
if a >= b + c:
    print('NAO FORMA TRIANGULO')
elif a * a == b * b + c * c:
    print('TRIANGULO RETANGULO')
elif a * a > b * b + c * c:
    print('TRIANGULO OBTUSANGULO')
    if a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')
elif a * a < b * b + c * c:
    print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')
elif a == b == c:
    print('TRIANGULO EQUILATERO')
elif a == b or a == c or b == c:
    print('TRIANGULO ISOSCELES')
