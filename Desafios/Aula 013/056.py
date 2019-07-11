"""
056
Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas.
No final do programa, mostre:
A media de idade do grupo
Qual o nome do homem mais velho.
Quantas mulheres tês menos de 20 anos
"""

Dados = [
    ["Kira", 25, "M"],
    ["Eren", 21, "M"],
    ["Asuna", 22, "F"],
    ["Mikasa", 20, "F]"]
]

media = 0
maior = -1
menores = 0
for i in range(len(Dados)):
    media += Dados[i][1]
    if Dados[i][2].lower() == "m":
        if maior == -1 or Dados[i][1] > Dados[maior][1]:
            maior = i
    else:
        if Dados[i][1] < 20:
            menores += 1

media = media / 4

print("A media de idades do grupo eh: {:.2f}".format(media))
if maior == -1:
    print("Nao possui homem no grupo")
else:
    print("O homem mais velho chama-se {} com {} anos".format(Dados[maior][0], Dados[maior][1]))
print("E possui {} mulher(es) com menos de 20 anos".format(menores))

