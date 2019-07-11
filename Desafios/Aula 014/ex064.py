"""
064
Crie um progra que leia vários numeros inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999.
No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desocnsiderando 999)
"""


count = 0
soma = 0
n = int(input("Digite um numero: "))
while(n != 999):
    soma += n
    count += 1
    n = int(input("Digite um numero: "))


print("Quantidade de valores lidos: {}".format(count))
print("A soma dos valores lidos: {}".format(soma))