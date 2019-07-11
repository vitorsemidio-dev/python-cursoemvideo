nome = input("Informe seu nome: ")
#20 alinhamento esquerda, centralizado e direta
print("Prazer em te conhecer, {:<20}!".format(nome)) #Alinhado a esquerda
print("Prazer em te conhecer, {:^20}!".format(nome)) #Centralizado
print("Prazer em te conhecer, {:>20}!".format(nome)) #Alinha a direita
print("Prazer em te conhecer, {:=^20}!".format(nome))


n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

soma = n1+n2
produto = n1*n2
divisao = n1/n2
divisaoInteira = n1 // n2
potencia = n1 ** n2

print("A soma eh {}, o produto eh {} e a divisao eh {}".format(soma, produto, divisao), end=" ")
print("Divisoa inteira {} e potencia {}".format(divisaoInteira, potencia))