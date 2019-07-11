"""
103
fichar (nome, gol)
return O jogador nome fez gol gols no campeonato
"""


def ficha (name='Te conheço?', gols=0):
    print(f"O jogador {name} marcou {gols} gols")



nome = str(input("Nome jogador: ")).strip()
gols = str(input("Gols no Campeonato: ")).strip()

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome != '':
    ficha(nome, gols)
else:
    ficha(gols=gols)