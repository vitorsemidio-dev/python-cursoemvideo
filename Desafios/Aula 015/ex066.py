"""
066
Crie um progra que leia vários numeros inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999.
No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desocnsiderando 999)
"""
contador = 0
soma = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    soma += n
    contador += 1


if contador == 0:
    print("Nao houve valores processados")
elif contador == 1:
    print("Soh teve um valor lido que foi {}".format(soma))
else:
    print("A soma dos {} valores lidos eh igual a {}".format(contador, soma))
