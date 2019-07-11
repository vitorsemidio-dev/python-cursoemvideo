"""
067
Faça um programa que mostre a tabuada de vários numeroes, um de cada vez, para cada valor digitado
O programa será interrompido quando o número solicitado for negativo.
"""

def tabuada (num):
    for i in range(11):
        x = num * i
        output = str(num) + " X " + str(i) + " = " + str(x)
        print("{:^25}".format(output))
        #print("{:<2} X {:>2} = {:>3}".format(num, i, x))



while True:
    n = int(input("Digite um numero: "))
    if n < 0:
        break
    texto = "Tabuada de " + str(n)
    print("{:=^25}".format(texto))
    tabuada(n)
    print("="*25)