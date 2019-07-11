"""
057
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "m" ou "f".
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexos = ["m", "M", "f", "j", "k", "m", "f", "L", "M", "F", "A", "f"]
i = 0
while (i < len(sexos)):
    if sexos[i].lower() == "m" or sexos[i].lower() == "f":
        print("\033[32mSexo {} informado eh valido\033[m".format(sexos[i]))
    else:
        print("\033[31mSexo {} informado eh invalido\033[m".format(sexos[i]))
    i += 1
print("\033[33mFIM\033[M")