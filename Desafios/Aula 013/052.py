from math import sqrt, ceil
from random import randint

def primo(num):
    if num <= 2:
        return num % 2 == 0
    if num % 2 == 0:
        return False
    for i in range(3, ceil(sqrt(num) + 0.5), 2):
        if num % i == 0:
            return False
    return True


#Gera array de numeros aleatorios
#qtdNumeros = int(input())
qtdNumeros = 30
numeros = []
for i in range(qtdNumeros):
    numeros.append(randint(0,1000))

for i in range(len(numeros)):
    print("{}: {}".format(numeros[i], primo(numeros[i])))