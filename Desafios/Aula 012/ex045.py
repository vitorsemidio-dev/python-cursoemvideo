from time import sleep
from random import randint

def jokenpo(jogador, computador):
    if jogador == computador:
        return 2
    elif jogador == 0:
        if computador == 1:
            return 1
        else:
            return 0
    elif jogador == 1:
        if computador == 0:
            return 0
        else:
            return 1
    else:
        if computador == 0:
            return 1
        else:
            return 0

text = {
    "fecha":"\033[m",
    "branco":"\033[30m",
    "vermelho":"\033[31m",
    "verde":"\033[32m",
    "amarelo":"\033[33m",
    "azul":"\033[34m",
    "roxo": "\033[35m",
    "ciano": "\033[36m",
    "cinza": "\033[37m",
}

game = True
while game:
    output = ["Parabens! Você ganhou", "Computador ganhou", "Empate"]
    opcoes = ["Pedra", "Papel", "Tesoura"]
    computador = randint(0,2)
    print('''Suas opções:
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura''')
    jogador = int(input("Qual a sua jogada? "))
    if jogador > 2 or jogador < 0:
        game = False
        continue
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")
    sleep(1)
    print("{}*".format("*-" * 20))
    if jokenpo(jogador, computador) == 2:
        print("{}{:^40}{}".format(text["amarelo"], output[2], text["fecha"]))
    elif jokenpo(jogador, computador) == 1:
        print("{}{:^40}{}".format(text["vermelho"], output[1], text["fecha"]))
    else:
        print("{}{:^40}{}".format(text["verde"], output[0], text["fecha"]))
    print("{}*".format("*-" * 20))
