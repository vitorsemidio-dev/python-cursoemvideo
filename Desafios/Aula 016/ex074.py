"""
074
Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

numeros = []
for i in range(5):
    numeros.append(randint(0, 100))

tupla = (numeros[0], numeros[1], numeros[2], numeros[3], numeros[4])


print(tupla)

maior = menor = tupla[0]

for i in range(1, len(tupla)):
    if tupla[i] > maior:
        maior = tupla[i]
    if tupla[i] < menor:
        menor = tupla[i]

print(f"O maior valor da tupla eh {maior}")
print(f"O menor valor da tupla eh {menor}")