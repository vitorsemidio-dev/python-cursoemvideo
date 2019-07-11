"""
080
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())
No final, mostre a lista ordenada na tela.
"""
from random import randint
numeros = []

for i in range(5):
    index = 0
    x = randint(0, 20)
    print(x, end=" ")
    if not len(numeros):
        numeros.append(x)
        continue
    for i in range(len(numeros)):
        if x < numeros[i]:
            break
        index += 1
    numeros.insert(index, x)

print()
print(numeros)


#5 10 15 11