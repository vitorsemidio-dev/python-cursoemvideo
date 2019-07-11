"""
088
Faça um programa que ajude um jogador da Mega Sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e
vai fsortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
"""
from random import randint, choice
from time import sleep

def printJogo(jogo):
    jogo.sort()
    for i in range(len(jogo)):
        print(f"{jogo[i]}", end=" ")
    print("")

qtdJogos = randint(1, 20)
#qtdJogos = 5

print("{}".format("-"*29))
print(f"{'-'*5} Sorteando {qtdJogos} Jogos {'-'*5}")
print("{}".format("-"*29))

for i in range(5):
    print(5-i, end=" ")
    sleep(1)
for i in range(3):
    print(".", end=" ")
    sleep(1)
print("")

for i in range(qtdJogos):
    espacoAmostral = list(range(1, 61))
    jogo = []
    for jogos in range(6):
        x = choice(espacoAmostral)
        espacoAmostral.remove(x)
        jogo.append(x)
    print(f"Jogo {i+1}: ", end="")
    printJogo(jogo)
    sleep(0.5)

print("Fim")


#testes
"""
x = list(range(1,61))
y = choice(x)
print(x)
print(y)
x.remove(y)
print(x)
"""