"""
070
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra.
b) quantos produtos custam mais de mil reais
c) qual é o nome do produto mais barato.
"""

from math import inf

i = 1
exa = 0
exb = 0
maisBarato = inf
while True:
    nome = str(input(f"Digite o nome do produto {i}: ")).strip()
    preco = float(input(f"Digite o preco do produto {i}: "))
    exa += preco
    if preco > 1000.0:
        exb += 1
    if preco < maisBarato:
        maisBarato = preco
        exc = nome

    resp = str(input("Deseja continuar: ")).strip().lower()
    if resp[0] != "s":
        break
    i+= 1

print(f"O total gasto na compra foi R${exa}")
print(f"Houve {exb} produto(s) acima de mil reais")
print(f"O nome do produto mais barato eh \033[32m{exc}\033[m custando \033[31m{maisBarato}\033[m")
