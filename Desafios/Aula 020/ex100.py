"""
100
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar().
A primeira função vai sortear cinco números e vai colocá-los dentro da lista e a segunda função vai
mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint

qtd = randint(5, 10)
def sorteio(lista, qtd):
    for i in range(qtd):
        x = randint(1,100)
        lista.append(x)


def somaPar(lista):
    soma = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            soma += lista[i]
    return soma


lista = []
sorteio(lista, qtd)
soma = somaPar(lista)

print(lista)
print(soma)


tam = len(lista)
for i in range(tam):
    if tam-i == 1:
        print(lista[tam-i-1])
        continue
    print(f"{lista[tam-i-1]} + ", end="")
    #print(lista[tam-i-1], end=" ")
#print(lista[tam-1])