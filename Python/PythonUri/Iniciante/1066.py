par = impar = posi = nega = 0

for c in range(0,5):
    n = int(input())
    if n %2 == 0:
        par += 1
    else:
        impar += 1
    if n > 0:
        posi += 1
    else:
        if n < 0:
            nega += 1

print(par, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(posi, "valor(es) positivo(s)")
print(nega, "valor(es) negativo(s)")
