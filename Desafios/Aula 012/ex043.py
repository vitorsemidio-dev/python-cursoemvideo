"""
043
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status
abaixo de 18.5: abaixo do peso
entre 18.5 e 25: peso ideal
entre 25 e 30: sobrepeso
entre 30 e 40: obsidade
acima de 40: obesidade morbida
"""


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

cores = [
    "\033[30m", #branco
    "\033[31m", #vermelho
    "\033[32m", #verde
    "\033[33m", #amarelo
    "\033[34m", #azul
    "\033[35m", #roxo
    "\033[36m", #ciano
    "\033[37m", #cinza
]

from time import sleep
def imcValor (massa, altura):
    return massa/pow(altura, 2)

def imcQ (massa, altura):
    result = massa/pow(altura, 2)
    if result < 18.5:
        return 0
    elif result < 25:
        return 1
    elif result < 30:
        return 2
    elif result < 40:
        return 3
    return 4

quadrosIMC = ["Abaixo do peso", "Peso ideal", "Sobrepeso", "Obsidade", "Obsidade Morbida"]
alturas = [1.54, 1.84, 1.66, 1.72, 1.67, 1.70, 1.70]
massas = [48, 72.5, 80.4, 62.8, 70, 90.1, 41.2]

for i in range(len(alturas)):
    print("{} Possuindo {} kg e {} m".format(i+1, massas[i], alturas[i]))
    print("{}{}".format(text["roxo"], "-=-" * 20))
    print("{}{:^60}".format(text["roxo"], "ANALISANDO"))
    print("{}{}{}".format(text["roxo"], "-=-" * 20, text["fecha"]))
    sleep(1)
    comeco = cores[imcQ(massas[i], alturas[i])]
    print("{}{:.2f} ---> {}{}".format(comeco, imcValor(massas[i], alturas[i]), quadrosIMC[imcQ(massas[i], alturas[i])], text["fecha"]))
    print("")
    #print("{:.2f} ---> {}".format(imcValor(massas[i], alturas[i])))




