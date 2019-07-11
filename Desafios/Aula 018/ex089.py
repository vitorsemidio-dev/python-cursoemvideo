"""
089
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e,
permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
from random import randint, random

def getNotas(idAluno):
    print(f"As notas do aluno {turma[idAluno][0]} foram: {turma[idAluno][1]} e {turma[idAluno][2]}")

alunos = ["Eren", "Mikasa", "Armin", "Levi", "Erwin", "Zeke",
               "Ichigo", "Orihime", "Yhwach", "Byakuya", "Renji", "Rukia",
               "Sakamoto", "Himiko", "Kira", "Oda",
               "Kirito", "Asuna", "Shino",
               "Elesis", "Lire", "Arme", "Lass", "Ryan", "Ronan", "Amy", "Jin", "Sieghart",
                "Mari", "Dio", "Zero", "Lupus", "Lin", "Azin", "Holy", "Edel", "Veigas", "Uno"]

notas = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0.0]
for i in range(10):
    notas[i] *= 1.0
    x = int(random()*100)
    notas.append(x/10)


qtdAlunos = randint(5, len(alunos))
#qtdAlunos = len(alunos)
#qtdAlunos = int(input("Digite a quantidade de alunos da turma: "))
#qtdAlunos = 5
turma = []
for i in range(qtdAlunos):
    nomeAluno = alunos[randint(0, len(alunos)) - 1]
    alunos.remove(nomeAluno)
    notaAAluno = notas[randint(0, len(notas)) - 1]
    notaBAluno = notas[randint(0, len(notas)) - 1]
    mediaAluno = (notaAAluno+notaBAluno) / 2

    turma.append([nomeAluno, notaAAluno, notaBAluno, mediaAluno])

print(f"{'Boletim Academico':-^30}")
print(f"{'id':<6}{'Nome':<16}{'Media':>8}")
for i in range(len(turma)):
    print(f"{i:<6}{turma[i][0]:<16}{turma[i][3]:>8.2f}")




print("Para vizualizar as notas do aluno, por favor, informe o id.")
print("Se digitar algum valor invalido, o programa sera encerrado")
while True:
    verNotas = int(input("ID aluno: "))
    if verNotas < 0 or verNotas >= qtdAlunos:
        break
    getNotas(verNotas)
