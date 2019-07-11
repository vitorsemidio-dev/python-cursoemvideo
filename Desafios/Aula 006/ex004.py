"""
    Faça um programa que leia algo pelo teclado e mostre na tela o
    seu tipo primitivo e todas as informações possível sobre ele
"""


algo = input("Digite algo: ")
print("Tipo do dado lido: {}".format(type(algo)))

print("Eh numero: {}".format(algo.isnumeric()))
print("Eh alfabetico: {}".format(algo.isalpha()))
print("Eh alfanumerico: {}".format(algo.isalnum()))
print("Eh digito: {}".format(algo.isdigit()))
print("Eh minusculo: {}".format(algo.islower()))
print("Eh maiusculo: {}".format(algo.isupper()))
print("Eh capitalizada: {}".format(algo.istitle()))