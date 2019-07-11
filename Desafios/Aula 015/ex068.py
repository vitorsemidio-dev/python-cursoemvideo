"""
068
Faça um programa que jogue par ou impar com o PC.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitorias consecutivas.
"""
from random import randint


def paridade (jogador, computador):
    x = jogador + computador
    string = ["par", "impar"]
    return string[x % 2]

vitorias = 0
while True:

    numComputador = randint(0,10)
    player = str(input("Deseja escolher par ou impar: ")).strip().lower()
    numJogador = int(input("Vai jogar qual numero: "))
    if player != paridade(numJogador, numComputador):
        break
    vitorias += 1

if vitorias == 0:
    print("O jogador ganhou nenhuma")
elif vitorias == 1:
    print("O jogador teve apenas uma vitoria")
else:
    print("O jogador teve {} vitorias consecutivas".format(vitorias))

