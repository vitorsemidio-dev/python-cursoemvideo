"""
098
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: inicio, fim e passo e realiza a contagem
Seu programa tem que realizar três contagens através da função criada:
a) de um até dez, de um em um
b) de dez até zero, de dois em dois
c) uma contagem personalizada
"""
from time import sleep
from random import randint

pausa = 0.5

def imprime(inicio, fim, passo):
    ultimo = 1
    if not passo:
        passo = 1
    if inicio > fim:
        passo = -abs(passo)
        ultimo = -1

    for i in range(inicio, fim+ultimo, passo):
        print(f"{i}", end=" ")
        sleep(pausa)
    print("")


def contador(inicio, fim, passo):
    print("Imprimindo de 1 a 10 com passo 1")
    imprime(1, 10, 1)

    print("Imprimindo de 10 até zero, de dois em dois")
    imprime(10, 0, -2)

    print("Isto aqui nao eh Yu-Gi-Oh! Mas eh sua vez")
    inicio = int(input(f"{'Inicio: ':<10}"))
    fim = int(input(f"{'Fim: ':<10}"))
    passo = int(input(f"{'Passo: ':<10}"))
    imprime(inicio, fim, passo)


contador(1,23,3)