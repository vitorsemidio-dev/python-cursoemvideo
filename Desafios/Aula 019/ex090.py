"""
090
Faça um programa que leia nome e média de um ano, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrturua na tela
"""
import random

alunos = ["Eren", "Mikasa", "Armin", "Levi", "Erwin", "Zeke",
               "Ichigo", "Orihime", "Yhwach", "Byakuya", "Renji", "Rukia",
               "Sakamoto", "Himiko", "Kira", "Oda",
               "Kirito", "Asuna", "Shino",
               "Elesis", "Lire", "Arme", "Lass", "Ryan", "Ronan", "Amy", "Jin", "Sieghart",
                "Mari", "Dio", "Zero", "Lupus", "Lin", "Azin", "Holy", "Edel", "Veigas", "Uno"]
notas = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0.0]

aluno = dict()
aluno["Nome"] = str(input("Digite o nome do aluno: "))
aluno["Média"] = float(input(f"Digite a média do aluno {aluno['Nome']}: "))
if aluno["Média"] >= 7:
    aluno["Situação"] = "Aprovado"
elif aluno["Média"] >= 5:
    aluno["Situação"] = "Recuperação"
else:
    aluno["Situação"] = "Reprovado"

print(aluno)
for chave, valor in aluno.items():
    print(f"{chave} eh {valor}")