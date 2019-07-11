"""
035
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
elas podem ou não formar um triângulo
"""
from termcolor import colored


def triangulo(a, b, c):
    if a * b * c <= 0:
        return False
    if a <= abs(b-c) or a > (b+c):
        return False
    return True


ladoA = int(input("Digite o lado A: "))
ladoB = int(input("Digite o lado B: "))
ladoC = int(input("Digite o lado C: "))


if triangulo(ladoA, ladoB, ladoC):
    print(colored("Eh possivel formar um triangulo com os lados {} {} {}".format(ladoA, ladoB, ladoC), "green"))
else:
    print(colored("Nao eh possivel formar um triangulo com os lados {} {} {}".format(ladoA, ladoB, ladoC), "red"))