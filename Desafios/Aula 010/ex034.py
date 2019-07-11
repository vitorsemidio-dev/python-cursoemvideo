"""
034
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salário superiores a R$1250,00 calcule um amento de 10%
Para os inferiores ou iguais, o aumento é de 15%
"""
from termcolor import colored

def attSalario(salario):
    if salario > 1250:
        return salario * 1.10
    return salario * 1.15

#salario = float(input("Digite o valor do seu salario: "))

salarios = [1250, 1500, 800, 900, 2000, 1000, 1300]
for i in range(len(salarios)):
    if salarios[i] > 1250:
        print(colored("Reajuste de 10%: ","red"), end="")
        #print(colored("Reajuste de 10%: ", "blue", end=" "))
        print(colored("{:.2f} ---> {:.2f}".format(salarios[i], attSalario(salarios[i])), "blue"))

    else:
        print(colored("Reajuste de 15%: ", "green"), end="")
        #print(colored("Reajuste de 15%: ", "green", end=""))
        print(colored("{:.2f} ---> {:.2f}".format(salarios[i], attSalario(salarios[i])), "blue"))
        #print("{:.2f} ---> {:.2f}".format(salarios[i], attSalario(salarios[i])))
