"""
085
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares
No final, mostre os valores pares e impares em ordem crescente.
"""

from random import randint

numeros = []
for i in range(7):
    numeros.append(randint(0,10))

pares = []
impares = []
paridade = [pares, impares]

for i in range(len(numeros)):
    paridade[numeros[i] % 2].append(numeros[i])
pares.sort()
impares.sort()
print(f"Pares: {pares}")
print(f"Impares: {impares}")

