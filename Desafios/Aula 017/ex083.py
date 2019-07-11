"""
083
Crie um programa onde o usuário digite uma expressão qualquer que usa parênteses.
Seu aplicativo deverá analiser se a expressão passada está com os parênteses abertos e fechados na ordem correta
"""

expressao = str(input("Digite sua expressoa: "))

flag = 0
for c in range(len(expressao)):
    if expressao[c] == "(":
        flag += 1
        continue
    if expressao[c] == ")":
        flag -= 1

    if flag < 0:
        break

if not flag:
    print(f"Expressao \033[32m{expressao}\033[m eh valida")
else:
    print(f"Expressao \033[31m{expressao}\033[m eh invalida")

