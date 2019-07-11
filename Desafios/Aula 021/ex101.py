"""
101
função voto(ano nascimento)
return negado ? opcional ? obrigatorio
"""
from datetime import date
from random import randint

def voto (anoNascimento):
    anoAtual = date.today().year
    idade = anoAtual - anoNascimento
    if idade < 16:
        print(f"Voto proibido para pessoa com {idade} anos")
    elif idade < 18 or idade > 70:
        print(f"Voto opcional para pessoa com {idade} anos")
    else:
        print(f"Voto obrigatorio para pessoa com {idade} anos")

vezes = randint(5, 10)
anoAtual = date.today().year

for i in range(vezes):
    anoNascimento = randint(1930, anoAtual)
    voto(anoNascimento)