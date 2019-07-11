jogador = {}
listaJogadores = []
#LEITURA DE DADOS
while True:
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
    listaJogadores.append(jogador.copy())
    resp = str(input("Deseja continuar? [S/N]")).strip().lower()
    while resp != "s" and resp != "n":
        resp = str(input("Deseja continuar? [S/N] ")).strip().lower()
    if resp == "s":
        continue
    break


for i in range(len(listaJogadores)):
    print(listaJogadores[i])

for i in range(len(listaJogadores)):
    qtdPatidas = len(listaJogadores[i]["Gols"])
    print(f"O jogador {listaJogadores[i]['Nome']} marcou {listaJogadores[i]['Total']} em {qtdPatidas}")
    for j in range(qtdPatidas):
        print(f"Na partida {j+1} marcou {listaJogadores[i]['Gols'][j]}")