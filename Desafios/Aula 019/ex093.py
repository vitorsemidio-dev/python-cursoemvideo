"""
093
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato
"""

jogador = {}


nome = str(input("Digite o nome do jogador: "))
partidas = int(input(f"Informe quantas partidas o {nome} jogo: "))

jogador["Nome"] = nome
jogador["Gols"] = []
total = 0
for i in range(partidas):
    gols = int(input(f"Gols da partida {i+1}: "))
    jogador["Gols"].append(gols)
    total += gols

jogador["Total"] = total

print(jogador)