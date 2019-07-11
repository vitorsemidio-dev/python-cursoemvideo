"""
059
Crie um programa que leia dois valores e mostre um menu na tela:
Somar
Multiplicar
Maior
Novos numeros
Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

def maior(a, b):
    if a > b:
        return a
    return b


while True:
    entrada = str(input("Digite dois valores: "))
    divisao = entrada.split(" ")
    a = int(divisao[0])
    b = int(divisao[1])

    print('''Escolha uma opcao abaixo:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa 
    ''')

    opcao = int(input("Sua opcao: "))
    if opcao == 1:
        print("A soma dos valores {} {} eh igual a {}".format(a, b, a+b))
    elif opcao == 2:
        print("O produto dos valores {} {} eh igual a {}".format(a, b, a*b))
    elif opcao == 3:
        print("O maior valor entre {} e {} eh {}".format(a, b, maior(a,b)))
    elif opcao == 4:
        continue
    elif opcao == 5:
        break