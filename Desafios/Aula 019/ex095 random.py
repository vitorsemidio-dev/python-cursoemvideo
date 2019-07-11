from random import randint, choice
from datetime import date
from time import sleep

text = {
    "vermelho":"\033[31m",
    "verde":"\033[32m",
    "amarelo":"\033[33m",
    "azul":"\033[34m"
}

def imprimirTabela(listaJogadores, cor):
    for i in range(len(listaJogadores)):
        print("{}{}".format(cor, "-"*35))
        qtdPatidas = len(listaJogadores[i]["Gols"])
        print(f"O jogador {listaJogadores[i]['Nome']} marcou {listaJogadores[i]['Total']} em {qtdPatidas}")
        for j in range(qtdPatidas):
            print(f"|{'=> Na partida':>15} {j + 1} marcou {listaJogadores[i]['Gols'][j]}{'|':>8}")
        print("{}\033[m".format("-" * 35))

nomesFemininos = ["Mikasa", "Orihime", "Rukia", "Himiko", "Asuna", "Shino",
               "Elesis", "Lire", "Arme", "Amy", "Mari", "Lin", "Holy", "Edel"]

nomesMasculinos = ["Eren", "Armin", "Levi", "Erwin", "Zeke", "Ichigo", "Yhwach", "Byakuya",
                   "Renji", "Sakamoto", "Kira", "Oda", "Kirito", "Lass", "Ryan", "Ronan",
                   "Jin", "Sieghart", "Dio", "Zero", "Lupus", "Azin", "Veigas", "Uno"]





jogador = {}
masculinoLista = []
femininoLista = []
generos = ["f", "m"]
qtdJogadores = randint(5, len(nomesFemininos) + len(nomesMasculinos)-1)
#qtdJogadores = 10

#LEITURA DE DADOS
while qtdJogadores:
    sexo = choice(generos)
    if sexo == "f" and len(nomesFemininos):
        nome = choice(nomesFemininos)
        nomesFemininos.remove(nome)
    elif sexo == "m" and len(nomesMasculinos):
        nome = choice(nomesMasculinos)
        nomesMasculinos.remove(nome)
    else:
        continue

    jogador["Nome"] = nome
    jogador["Gols"] = []
    total = 0
    partidas = randint(0, 5)
    for i in range(partidas):
        gols = randint(0,5)
        jogador["Gols"].append(gols)
        total += gols

    jogador["Total"] = total
    if sexo == "f":
        femininoLista.append(jogador.copy())
    else:
        masculinoLista.append(jogador.copy())

    qtdJogadores -= 1

print("TABELA MASCULINA")
imprimirTabela(masculinoLista, text["azul"])
print("\n\nTABELA FEMININA")
imprimirTabela(femininoLista, text["vermelho"])
