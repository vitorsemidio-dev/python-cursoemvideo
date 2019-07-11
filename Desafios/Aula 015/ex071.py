"""
071
Crie um programa que simule o funcionamento de um caixa eletrônico.
no início, pergunte ao usuário qual será o valor a ser sacado
e o programa vai informar quantas cédulas de cada valor serão entregues.
obs: considere que o caixa possua cédulas de 50 20 10 e 1
"""

def sacar(valorSaque, cedulasDisponiveis):
    for i in range(len(cedulas)):
        notas = valorSaque // cedulasDisponiveis[i]
        print(f"{notas} notas de R${cedulasDisponiveis[i]}")
        valorSaque = valorSaque % cedulas[i]
cedulas = [50, 20, 10, 1]
saque = int(input("Digite o valor que deseja sacar: "))

sacar(saque, cedulas)