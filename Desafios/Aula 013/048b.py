
inicio = 1
fim = 500

primeiro = inicio + 3 - (inicio%3)

soma = 0
for i in range(primeiro, fim+1, 6):
    soma += i

print(soma)

