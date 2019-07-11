from random import random, randint
from time import sleep


nomes = ["Eren", "Mikasa", "Armin", "Levi", "Erwin", "Zeke",
               "Ichigo", "Orihime", "Yhwach", "Byakuya", "Renji", "Rukia",
               "Sakamoto", "Himiko", "Kira", "Oda",
               "Kirito", "Asuna", "Shino",
               "Elesis", "Lire", "Arme", "Lass", "Ryan", "Ronan", "Amy", "Jin", "Sieghart",
                "Mari", "Dio", "Zero", "Lupus", "Lin", "Azin", "Holy", "Edel", "Veigas", "Uno"]
notas = [0.0, 10.0]

for i in range(10):
    x = float(randint(0,10))
    notas.append(x)
    x = int(random()*100)
    notas.append(x/10)

n = int(input("Aleatorio [ 0 ], Valor fixo [ 1 ], Usuario [ 2 ]: "))
if not n:
    qtdAluno = randint(5,len(nomes)-1)
elif n == 1:
    qtdAluno = int(input("Quantidade de alunos da turma: "))
    #qtdAluno = 2
else:
    n = 5
turma = list()
aluno = dict()

for i in range(qtdAluno):
    nomeAleatorio = nomes[randint(0,len(nomes) - 1)]
    nomes.remove(nomeAleatorio)
    p1 = notas[randint(0, len(notas) - 1)]
    p2 = notas[randint(0, len(notas) - 1)]
    media = (p1+p2) / 2

    aluno["Nome"] = nomeAleatorio
    aluno["P1"] = p1
    aluno["P2"] = p2
    aluno["Média"] = media
    turma.append(aluno.copy())

print(f"{'ID':^5}{'Nome':<15}{'Nota 1':^8}{'Nota 2':^8}{'Média':^8}")
for i in range(len(turma)):
    print(f"{i:^5}", end="")
    for chave, valor in turma[i].items():
        if type(valor) == str:
            print(f"{valor:<15}", end="")
        else:
            print(f"{valor:^8.2f}", end="")
    sleep(1)

    print("")