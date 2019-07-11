"""
081
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma decrescente.
c) se o valor cinco foi digitado e está ou não na lista.
"""

from random import randint

qtd = randint(5,20)
numeros = []
for i in range(qtd):
    numeros.append(randint(0, 10))

print(f"Foram lidos {qtd} valores")
numeros.sort(reverse=True)
print(f"A lista em ordem decrescente: {numeros}")
if 5 in numeros:
    print(f"O valor 5 aparece na posicao {numeros.index(5) + 1}")
else:
    print(f"O valor 5 nao aparece")