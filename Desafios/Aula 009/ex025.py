"""
025
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
"""

def existeNome(ref, nome):
    divisao = nome.lower().split()
    for i in range(len(divisao)):
        if divisao[i][:len(ref)] == ref.lower():
            return True
    return False


nome = str(input("Digite seu nome completo: ")).strip()
comparacao = "silva"


if (existeNome(comparacao, nome)):
    print("O nome {} possui \"{}\"".format(nome, comparacao))
else:
    print("O nome {} não possui \"{}\"".format(nome, comparacao))