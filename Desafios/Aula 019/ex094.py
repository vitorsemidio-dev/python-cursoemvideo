"""
094
Crie um programa que leia nome, sexo de idade de várias pessoas
Guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista
No final, mostre:
a) quantas pessoas foram cadastradas
b) a média de idade do grupo
c) uma lista com todas as mulheres
d) uma lista com todas as pessoas com idade acima da média
"""
from random import randint, choice

def fMedia (mediaAntiga, novoValor, termos):
    return (mediaAntiga * (termos -1) + novoValor) / termos

nomesFemininos = ["Mikasa", "Orihime", "Rukia", "Himiko", "Asuna", "Shino",
               "Elesis", "Lire", "Arme", "Amy", "Mari", "Lin", "Holy", "Edel"]

nomesMasculinos = ["Eren", "Armin", "Levi", "Erwin", "Zeke", "Ichigo", "Yhwach", "Byakuya",
                   "Renji", "Sakamoto", "Kira", "Oda", "Kirito", "Lass", "Ryan", "Ronan",
                   "Jin", "Sieghart", "Dio", "Zero", "Lupus", "Azin", "Veigas", "Uno"]

#nomesFemininos = ["Mikasa", "Orihime", "Rukia"]
#nomesMasculinos = ["Eren", "Armin", "Levi", "Erwin", "Zeke"]

#a b c d
pessoasCadastradas = 0
mediaIdade = 0
listaMulheres = []
listaIdosos = []


lista = []
cadastro = {}
qtdCadastro = randint(15, len(nomesMasculinos) + len(nomesFemininos) - 1)
#qtdCadastro = 5
generos = ["M", "F"]

contador = 0
while contador < qtdCadastro:
    sexo = choice(generos)
    age = randint(5, 35)
    if sexo == "M" and len(nomesMasculinos):
        cadastro["Nome"] = choice(nomesMasculinos)
        nomesMasculinos.remove(cadastro["Nome"])
        cadastro["Sexo"] = sexo
        cadastro["Idade"] = age
        lista.append(cadastro.copy())
    elif sexo == "F" and len(nomesFemininos):
        cadastro["Nome"] = choice(nomesFemininos)
        nomesFemininos.remove(cadastro["Nome"])
        cadastro["Sexo"] = sexo
        cadastro["Idade"] = age
        lista.append(cadastro.copy())
    else:
        print(sexo, end=" ")
        continue
    contador += 1

print("")

for i in range(len(lista)):
    print(lista[i])

pessoasCadastradas = len(lista)
for i in range(len(lista)):
    mediaIdade = fMedia(mediaIdade, lista[i]["Idade"], i+1)
    if lista[i]["Sexo"] == "F":
        listaMulheres.append(lista[i].copy())

for i in range(pessoasCadastradas):
    if lista[i]["Idade"] >= mediaIdade:
        listaIdosos.append(lista[i].copy())



print(f"Ao todo, temos {pessoasCadastradas} pessoas cadastradas")
print(f"A media de idade eh {mediaIdade:.2f} anos")
print(f"Os nomes das mulheres cadastradas sao: ", end="")
for i in range(len(listaMulheres)):
    print(listaMulheres[i]["Nome"], end=" ")


print(f"\nOs nomes das pessoas acima da media: ", end="")
for i in range(len(listaIdosos)):
    print(listaIdosos[i]["Nome"], end=" ")
