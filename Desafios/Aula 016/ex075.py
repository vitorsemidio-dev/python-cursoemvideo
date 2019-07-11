"""
075
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a) quantas vezes apareceu o valor nove.
b) em que posição foi digitado o primeiro valor 3.
c) quais foram os números pares
"""

from random import randint


def indice(procura, tupla):
    for pos, item in enumerate(tupla):
        if procura == item:
            return pos
    return -1

numeros = []
for i in range(4):
    numeros.append(randint(0,10))

tupla = (numeros[0], numeros[1], numeros[2], numeros[3])
exa = tupla.count(9)
exb = indice(3, tupla)
exc = []

print(tupla)
print(f"O numero 9 apareceu: {exa}")
print(f"O valor 3 apareceu pela primeiros vez na posicao {exb}" if exb >= 0 else "Nao ha numero 3 na tupla")
for num in tupla:
    if num % 2 == 0:
        exc.append(num)

if len(exc):
    print("O(s) numero(s) pare(s) são: ", end="")
    for num in exc:
        print(num, end=" ")
    print("")
else:
    print("Nao há numeros pares!")