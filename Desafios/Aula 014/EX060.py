"""
060
Faça um programa que calcule o fatorial de um numero
"""

from random import randint

def fatorial (num):
    if num == 0:
        return 1
    return num * fatorial(num-1)

numeros = []

for i in range(randint(5, 20)):
    numeros.append(randint(2, 15))

for i in range(len(numeros)):
    print("{}! = {}".format(numeros[i], fatorial(numeros[i])))