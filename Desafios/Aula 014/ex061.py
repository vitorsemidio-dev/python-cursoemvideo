"""
061
Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os
dez primeiros termos da PA usando while
"""

primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razao da PA: "))

i = 0
while (i < 10):
    termo = primeiro + razao * i
    print("{}".format(termo), end=" ")
    i+=1

print("\nFIM")