"""
069
Crie um programa que leia a idade e sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário qr continuar ou não.
No final, mostre:
a) quantas pessoas têm mais de dezoito anos.
b) quantos homens focam cadastrados.
c) quantas mulheres têm menos de 20 anos
"""


exA = exB = exC = 0
i = 1
while True:
    print("Dados da Pessoa {}".format(i))
    idade = int(input("Digite a idade da pessoa {}: ".format(i)))
    sexo = str(input("Digite o sexo da pessoa {}: ".format(i))).strip().lower()
    if idade > 18:
        exA += 1
    if sexo == "m":
        exB += 1
    else:
        if idade < 20:
            exC += 1
    resp = str(input("Deseja continuar: ")).strip().lower()

    if resp[0] != "s":
        break
    i+=1


print("{} pessoas têm mais de 18 anos".format(exA))
print("{} homens cadastrados com sucesso".format(exB))
print("{} mulheres têm menos de 20 anos".format(exC))
print(f"{exC} mulheres têm menos de 20 anos.")