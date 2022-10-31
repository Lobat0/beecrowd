x = int(input())
y = int(input())
soma = 0

if x > y:
    for c in range(y+1, x):
        """print(c)"""
        if c % 2 == 1:
            soma += c



if y > x:
    for i in range(x+1, y):
        """print(i)"""
        if i % 2 == 1:
            soma += i

print(soma)
