def dividido (string):
    for i in range(5):
        divisao = string[i].split()
        print(divisao)

anime = []
for i in range(5):
    ler = str(input("Digite o nome do anime {}: ".format(i+1)))
    anime.append(ler)

#print(anime)
dividido(anime)
"""
Shingeki no Kyojin
Death Note
Boku no Hero
Sword Art Online
Dragon Ball Super
"""