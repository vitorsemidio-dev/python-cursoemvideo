"""
092
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date


cadastro = dict()
contribuicaoMinima = 35
ano = date.today().year

cadastro["Nome"] = str(input("Digite seu nome: "))
anoNascimento = int(input("Ano de Nascimento: "))
cadastro["Idade"] = ano - anoNascimento
CTPS = int(input("Numero da CTPS (0 se não possuir): "))

if CTPS:
    cadastro["Ano Contratacao"] = int(input("Digite o ano de contratacao: "))
    cadastro["Salario"] = float(input("Informe seu salario: "))
    cadastro["Idade Aposentadoria"] = cadastro["Ano Contratacao"] + contribuicaoMinima - anoNascimento

for chave, valor in cadastro.items():
    print(f"{chave} eh {valor}")