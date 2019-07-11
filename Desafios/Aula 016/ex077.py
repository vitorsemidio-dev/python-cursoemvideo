"""
077
Crie um programa que tenha uma tupla com várias palavras.
Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.
"""


personagens = ("Eren", "Mikasa", "Armin", "Levi", "Erwin", "Zeke",
               "Ichigo", "Orihime", "Yhwach", "Byakuya", "Renji", "Rukia",
               "Sakamoto", "Himiko", "Kira", "Oda",
               "Kirito", "Asuna", "Shino",
               "Elesis", "Lire", "Arme", "Lass", "Ryan", "Ronan", "Amy")


vogais = "aeiou"

for nome in personagens:
    print(f"O nome {nome} possui as seguintes vogais: ", end="")
    for i in range(len(nome)):
        if nome[i].lower() in vogais:
            print(nome[i], end=" ")
    print("")
