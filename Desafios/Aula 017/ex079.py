"""
079
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já existe lá dentro, ele não será adicionado.
No f inal, serão exibidos todos o valores únicos digitados em ordem crescente
"""

from random import randint

qtd = randint(5, 20)
numeros = []
for i in range(qtd):
    x = randint(0, 20)
    if x in numeros:
        print(f"\033[31mO valor {x} jah existe na lista. Portanto, ele não foi adicionado\033[m")
        continue

    numeros.append(x)
print(f"Foram lidos {qtd} numeros")
print(f"Os valores lidos ordenados: ", end="")
numeros.sort()
for num in numeros:
    print(f"\033[34m{num}", end=" ")
