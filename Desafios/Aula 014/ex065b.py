"""
065
Crie um programa que leia vários numeros inteiros pelo teclado. No final da execução, mostre
a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
from time import sleep
from math import inf

def fMedia(mediaAntiga, novoValor, termos):
    if termos == 1:
        return novoValor*1.0
    mediaNova = (mediaAntiga * (termos-1) + novoValor) / (termos) * 1.0
    return mediaNova

media = 0
maior = -inf
menor = inf
qtdValoresLidos = 0

while True:
    n = int(input("Digite um numero: "))
    while n:
        qtdValoresLidos += 1
        media = fMedia(media, n, qtdValoresLidos)

        if n > maior:
            maior = n
        if n < menor:
            menor = n
        n = int(input("Digite um numero: "))

    if not qtdValoresLidos:
        print("Nenhum valor registrado")
    else:
        print("A media ateh o momento eh: {:.2f}".format(media))
        print("O maior valor lido ateh o momento eh: {}".format(maior))
        print("O menor valor lido ateh o momento eh: {}".format(menor))

    continuar = int(input("Deseja continuar: [ 1 - Sim ] ou [ 0 - Não ]\n"))
    if not continuar:
        print("Finalizando programa")
        sleep(1)
        print("Fim")
        break