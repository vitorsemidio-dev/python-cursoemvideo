from datetime import date

def categoria (idade):
    if idade <= 9:
        return 0
    elif idade <= 14:
        return 1
    elif idade <= 19:
        return 2
    elif idade <= 20:
        return 3
    else:
        return 4

categorias = ["Mirim", "Infantil", "Junior", "Senior", "Master"]

#anoNascimento = int(input("Digite o seu ano de nascimento: "))
#idade = date.today().year - anoNascimento
Nascimentos = [1990, 2015, 2011, 1998, 2006, 1999, 1998, 1997]
for i in range(len(Nascimentos)):
    idade = date.today().year - Nascimentos[i]
    print("Quem nasceu em {} pertence a categoria {}".format(Nascimentos[i], categorias[categoria(idade)]))


