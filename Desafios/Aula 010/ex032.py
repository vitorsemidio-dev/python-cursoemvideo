from datetime import date


def bissexto(ano):
    if not (ano % 4):
        if not (ano % 100):
            return (ano % 400) == 0
        return True
    return False


#ano = int(input("Digite um ano: "))
anos = [1996, 2000, 2004, 2015, 2016, 2100, 2200, 2300, 2400, 0, 500]
for i in range(len(anos)):
    if not anos[i]:
        anoAtual = date.today().year
        print("{}: eh bissexto".format(anoAtual) if bissexto(anoAtual) else "{}: nao eh bissexto".format(anoAtual))
        continue
    print("{}: eh bissexto".format(anos[i]) if bissexto(anos[i]) else "{}: nao eh bissexto".format(anos[i]))