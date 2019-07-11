"""
096
Faça um program que tenha uma função chamada área(), que recebe as
dimensões de um terreno retangular e mostre a área do terreno.
"""
from random import randint
def calcularArea(altura, largura):
    return altura * largura


altura = randint(1, 20)
largura = randint(1, 20)
area = calcularArea(altura, largura)

print(f"Um terreno {altura} X {largura} possui {area}m²")