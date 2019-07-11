from random import randint, choice
from time import sleep

def escreve(string):
    tam = len(string)
    tam += 2
    linha = "-"*(tam)
    print(linha)
    print(f"|{string}|")
    print(linha)


animes = [
        "Shingeki no Kyojin", "Dragon Ball Super", "Death Note", "Boku no Hero Academia", "Naruto",
        "One Piece", "Digimon Adventure", "Cardcaptor Sakura Clear Card-hen", "InuYasha Kanketsu-hen"
]

qtdAleatorio = randint(5, len(animes)-1)

for i in range(qtdAleatorio):
    string = choice(animes)
    animes.remove(string)
    escreve(string)
    print("")
    sleep(1)