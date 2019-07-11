"""
058
Melhore o jogo do desafio 028 onde o jogador vai pensar em um numero entre 0 e 10
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
"""

from random import randint
from time import sleep
from termcolor import colored
computador = randint(0, 10)
print(computador)

print(colored('-=-', 'yellow') * 20)
frase = "Eu escolhi um numero entre 0 e 10. Tente adivinhar"
print(colored("{:^60}".format(frase), 'blue'))

print(colored('-=-', 'yellow') * 20)

jogador = int(input("Em qual numero pensei? "))
tentativa = 1
print("PROCESSANDO...")
while(jogador != computador):
    sleep(1)
    print("{}ERROU! Tente novamente!{}".format("\033[31m", "\033[m"))
    tentativa += 1
    jogador = int(input("Em qual numero pensei? "))
    print("PROCESSANDO...")
sleep(1)
if tentativa == 1:
    print("{}Parabens! Você acertou de primeira{}".format("\033[32m", "\033[m"))
else:
    print("{}Parabens! Você acertou em {} tentativas{}".format("\033[34m",tentativa, "\033[m"))
