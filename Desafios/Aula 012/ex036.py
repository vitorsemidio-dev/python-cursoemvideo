from time import sleep

text = {
    "fecha":"\033[m",
    "branco":"\033[30m",
    "vermelho":"\033[31m",
    "verde":"\033[32m",
    "amarelo":"\033[33m",
    "azul":"\033[34m",
    "roxo": "\033[35m",
    "ciano": "\033[36m",
    "cinza": "\033[37m",
}

back = {
    "fecha":"\033[m",
    "branco":"\033[40m",
    "vermelho":"\033[41m",
    "verde":"\033[42m",
    "amarelo":"\033[43m",
    "azul":"\033[44m",
    "roxo": "\033[45m",
    "ciano": "\033[46m",
    "cinza": "\033[47m",
}

style = {
    "fecha":"\033[m",
    "negrito":"\033[1",
    "italico":"\033[4",
    "invertido":"\033[7",
}

def aprovaEmprestimo(valor, tempo, salario):
    if salario*0.3 >= (valor / (tempo*12)):
        return True
    return False

entrada = input("Digite o valor da casa, seu salario e em quantos anos pretende pagar: ")
divisao = entrada.split(" ")
casa = float(divisao[0])
salario = float(divisao[1])
anos = int(divisao[2])

prestacao = casa / (anos*12)


print("Para pagar uma casa no valor de R${:.2f} em {} terá prestação no valor de {:.2f}".format(casa, anos, prestacao))
print("{}{}{}".format(text["amarelo"], "-=-" * 20, text["fecha"]))
print("{}{:^60}{}".format(text["amarelo"], "ANALISANDO A SITUAÇÃO", text["fecha"]))
print("{}{}{}".format(text["amarelo"], "-=-" * 20, text["fecha"]))
sleep(3)

if aprovaEmprestimo(casa, anos, salario):
    print("{}Parabens! Emprestimo aprovado{}".format(text["verde"], text["fecha"]))
else:
    print("{}Emprestimo Negado{}".format(text["vermelho"], text["fecha"]))
