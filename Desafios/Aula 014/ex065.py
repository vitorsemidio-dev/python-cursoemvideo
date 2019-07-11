"""
065
Crie um programa que leia vários numeros inteiros pelo teclado. No final da execução, mostre
a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""


def fMedia(mediaAntiga, novoValor, termos):
    if termos == 1:
        return novoValor*1.0
    mediaNova = (mediaAntiga * (termos-1) + novoValor) / (termos) * 1.0
    return mediaNova

media = 0
contador = 0
medias = [8, 6, 10, 4]
for i in range(len(medias)):
    media = fMedia(media, medias[i], i+1)
    print("{}".format(media))
