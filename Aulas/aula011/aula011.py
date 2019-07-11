animes = ["Shingeki no Kyojin", "Dragon Ball Super", "Death Note"]
print("\033[1;35;44m{}\033[m\n\033[4;31;47m{}\033[m\n\033[1;30;45m{}\033[m".format(animes[0], animes[1], animes[2]))
#print("\033[1;31;43mOla, mundo!")
print("\033[1;32;44mShingeki no Kyojin")
print("{}{}{}".format("\033[1;32;44m", "Shingeki no Kyojin", "\033[m"))

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
print("{}{}{}{}".format(text["verde"], back["roxo"], "Shingeki no Kyojin", text["fecha"]))