"""
051
Desenvolva um programa que leia o primeiro termo e a razão de uma Pa.
No final mostre os dez primeiros termos dessa progressao
"""


primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razao da PA: "))
print("Os 10 primeiros termos da PA: ", end="")
for i in range(10):
    print("{}".format(primeiro + i*razao), end=" ")