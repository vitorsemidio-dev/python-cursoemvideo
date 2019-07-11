from random import randint
from time import sleep
from termcolor import colored

print(colored('-=-', 'yellow') * 20)
frase = "Eu escolhi um numero entre 0 e 5. Tente adivinhar"
print(colored("{:^60}".format(frase), 'blue'))
computador = randint(0, 5)
print(colored('-=-', 'yellow') * 20)

jogador = int(input("Em qual numero pensei? "))

print("PROCESSANDO...")
sleep(2)
if jogador == computador:
    print(colored("Parabens! Você acertou", 'green'))
else:
    print(colored("Eu ganhei! Eu pensei no numero {} e nao no {}".format(computador, jogador), "red"))