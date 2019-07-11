"""
062
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais quantos termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao da PA: "))
fim = 0
i = 0
while True:
    termos = int(input("Deseja mostrar mais quantos termos: "))
    fim += termos
    if not termos:
        break
    while i < fim:
        x = primeiro + razao * i
        i+=1
        print("{}".format(x), end=" ")
    print("")

print("Fim")