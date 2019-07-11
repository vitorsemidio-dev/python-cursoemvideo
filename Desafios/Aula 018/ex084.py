"""
084
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:

a) quantas pessoas foram cadastradas.
b) uma listagem com as pessoas mais pesadas.
c) uma listagem com as pessoas mais leves.
"""

from random import randint

personagens = ["Eren", "Mikasa", "Armin", "Levi", "Erwin", "Zeke",
               "Ichigo", "Orihime", "Yhwach", "Byakuya", "Renji", "Rukia",
               "Sakamoto", "Himiko", "Kira", "Oda",
               "Kirito", "Asuna", "Shino",
               "Elesis", "Lire", "Arme", "Lass", "Ryan", "Ronan", "Amy"]

#pesos = [85.6, 91, 58, 46, 91.1, 44.4, 68, 115, 66.3, 51, 59, 88, 89, 81.9]
pesos = [50, 65, 65, 40, 65, 65, 70, 80, 80, 80, 40, 40, 40, 40]

#qtdNomes = randint(5,len(personagens))
qtdNomes = len(personagens)
qtdPesos = len(pesos)
qtdCadastro = randint(5, 20)
cadastro = [[], []]

for i in range(qtdCadastro):
    nomeRandom = personagens[randint(0, qtdNomes-1)]
    pesoRandom = pesos[randint(0, qtdPesos-1)]
    cadastro[0].append(nomeRandom)
    cadastro[1].append(pesoRandom)

print(f"{'Pessoas cadastradas':.^50}")

for i in range(qtdCadastro):
    #print("Nome: {} // Idade: {}".format(cadastro[0][i], cadastro[1][i]))
    #print(f"Nome: {cadastro[0][i]} Idade: {cadastro[1][i]}")
    print(f"Personagem {cadastro[0][i]} possui {cadastro[1][i]} kg")



print(f"Quantidade de pessoas cadastradas: {len(cadastro[0])}")

maiorPeso = max(cadastro[1])
menorPeso = min(cadastro[1])

pesados = []
leves = []

for i in range(qtdCadastro):
    if cadastro[1][i] == maiorPeso:
        pesados.append(cadastro[0][i])
        continue
    if cadastro[1][i] == menorPeso:
        leves.append(cadastro[0][i])
        continue

print(f"Os mais pesados com {maiorPeso} são: {pesados}")
print(f"Os mais pesados com {menorPeso} são: {leves}")