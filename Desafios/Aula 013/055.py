"""
055
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor dos pesos lidos
"""

def max (a, b):
    if a >= b:
        return a
    return b
def min (a, b):
    if a <= b:
        return a
    return b

pesos = [48, 50, 96, 75, 80]
maior = pesos[0]
menor = pesos[0]
for i in range(len(pesos)):
    maior = max(maior, pesos[i])
    menor = min(menor, pesos[i])

print("{} {}".format(maior, menor))