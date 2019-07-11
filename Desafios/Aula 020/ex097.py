"""
097
Faça um programa que tenha uma função chamada escreve(),
que recebe um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável
ex: escrava(olá, mundo)
------------
 olá, mundo
------------
"""

def escreve(string):
    tam = len(string)
    tam += 2
    linha = "-"*(tam)
    print(linha)
    print(f" {string}")
    print(linha)

string = str(input("Digite sua frase: "))
escreve(string)