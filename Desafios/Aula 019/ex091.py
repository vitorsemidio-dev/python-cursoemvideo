"""
091
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter
nomes = ["Eren", "Mikasa", "Armin", "Levi", "Erwin", "Zeke",
               "Ichigo", "Orihime", "Yhwach", "Byakuya", "Renji", "Rukia",
               "Sakamoto", "Himiko", "Kira", "Oda",
               "Kirito", "Asuna", "Shino",
               "Elesis", "Lire", "Arme", "Lass", "Ryan", "Ronan", "Amy", "Jin", "Sieghart",
                "Mari", "Dio", "Zero", "Lupus", "Lin", "Azin", "Holy", "Edel", "Veigas", "Uno"]
jogadores = []

jogo = {
    nomes[randint(0,len(nomes)-1)]: randint(1,6),
    nomes[randint(0,len(nomes)-1)]: randint(1,6),
    nomes[randint(0,len(nomes)-1)]: randint(1,6),
    nomes[randint(0,len(nomes)-1)]: randint(1,6),
}
ranking = list()
"""
qtdJogadores = 5 #randint(3, 10)

for i in range(qtdJogadores):
    jogo["Nome"] = nomes[randint(0, len(nomes) - 1)]
    nomes.remove(jogo["Nome"])
    jogo["Dado"] = randint(1, 6)
    jogadores.append(jogo.copy())


for i in range(len(jogadores)):
    #print(f"{ 'O(A) '+str(jogadores[i]['Nome'])+' tirou '+str(jogadores[i]['Dado'])+' no dado' }")
    print(f"O(A) {jogadores[i]['Nome']} tirou {jogadores[i]['Dado']} no dado")
    sleep(1)
"""

for nome, dado in jogo.items():
    print(f"{nome} tirou {dado}")
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(ranking)
for pos, dic in enumerate(ranking):
    print(f"{pos+1} lugar: {dic[0]} com {dic[1]}")
    sleep(0.5)

#print(ranking)
"""
for i in range(len(ranking)):
    print(f"O(A) {jogadores[i]['Nome']} tirou {jogadores[i]['Dado']} no dado")
    sleep(1)
"""