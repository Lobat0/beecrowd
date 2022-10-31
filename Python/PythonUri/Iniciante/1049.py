pala1 = input().lower()
pala2 = input().lower()
pala3 = input().lower()
animal = ''
if pala1 == 'vertebrado':
    if pala2 == 'ave':
        if pala3 == 'carnivoro':
            animal = 'aguia'
        else:
            animal = 'pomba'
    else:
        if pala3 == 'onivoro':
            animal = 'homem'
        else:
            animal = 'vaca'
else:
    if pala2 == 'inseto':
        if pala3 == 'hematofago':
            animal = 'pulga'
        else:
            animal = 'lagarta'
    else:
        if pala3 == 'hematofago':
            animal = 'sanguessuga'
        else:
            animal = 'minhoca'
print(animal)