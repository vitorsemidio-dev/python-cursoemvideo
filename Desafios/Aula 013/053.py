"""
053
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
ex:
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona
"""

def palindromo(frase):
    pali = []

    for i in range(len(frase)):
        if frase[i] != " ":
            pali.append(frase[i])
    tamanho = len(pali)-1
    for i in range(len(pali) // 2):
        if pali[i] != pali[tamanho-i]:
            return False
    return True

frase = str(input("Digite uma frase: ")).strip().lower()


print("{}".format(palindromo(frase)))

