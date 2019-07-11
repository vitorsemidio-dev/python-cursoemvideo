
from datetime import date
from random import randint, choice


nomes = ["Eren", "Mikasa", "Armin", "Levi", "Erwin", "Zeke",
               "Ichigo", "Orihime", "Yhwach", "Byakuya", "Renji", "Rukia",
               "Sakamoto", "Himiko", "Kira", "Oda",
               "Kirito", "Asuna", "Shino",
               "Elesis", "Lire", "Arme", "Lass", "Ryan", "Ronan", "Amy", "Jin", "Sieghart",
                "Mari", "Dio", "Zero", "Lupus", "Lin", "Azin", "Holy", "Edel", "Veigas", "Uno"]
salarios = [850, 430, 1500, 2500, 3600, 1250, 700, 620, 380, 2200]


cadastro = dict()
contribuicaoMinima = 35
faixaIdade = 50
idadeMinimaParaTrabalhar = 10
anoAtual = date.today().year
#qtdCadastros = randint(5, len(nomes)-1)
qtdCadastros = 20

gafanhotoTrabalhando = []
gafanhotoEstudando = []

for i in range(qtdCadastros):
    cadastro["Nome"] = choice(nomes)
    nomes.remove(cadastro["Nome"])
    anoNascimento = randint(anoAtual - faixaIdade, anoAtual - idadeMinimaParaTrabalhar)
    cadastro["Idade"] = anoAtual - anoNascimento

    CTPS = randint(0,1)

    if CTPS:
        cadastro["Ano Contratacao"] = randint(anoNascimento + idadeMinimaParaTrabalhar, anoAtual)
        cadastro["Salario"] = choice(salarios)
        cadastro["Idade Aposentadoria"] = cadastro["Ano Contratacao"] + contribuicaoMinima - anoNascimento
        gafanhotoTrabalhando.append(cadastro.copy())
        del(cadastro["Salario"])
        del(cadastro["Ano Contratacao"])
        del(cadastro["Idade Aposentadoria"])
    else:
        gafanhotoEstudando.append(cadastro.copy())

print("Estudando")
for i in range(len(gafanhotoEstudando)):
    print(gafanhotoEstudando[i])

print("Trabalhando")
for i in range(len(gafanhotoTrabalhando)):
    print(gafanhotoTrabalhando[i])

