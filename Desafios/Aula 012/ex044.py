def calcularValor(valor, opcao):
    taxas = [-0.10, -0.05, 0, 0.20]
    pagamento = valor * (1+taxas[opcao-1])
    return pagamento
"""
valor = float(input("Digite o valor do produto: "))
print('''Formas de Pagamento
[ 1 ] À Vista no Cheque/Dinheiro
[ 2 ] À Vista no Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou + no Cartão
''')
opcao = int(input("Sua opcao: "))
"""

valores = [800, 900, 1500, 3600, 100, 25, 750, 2150, 2150, 2150]
opcoes = [1, 4, 3, 3, 2, 1, 2, 4, 3, 2]

textos = ["10% de desconto", "5% de desconto", "preço normal", "20% de juros"]

for i in range(len(valores)):
    print( "R${:.2f} terá {}. Voce ira pagar R${:.2f}".format(valores[i]*1.00, textos[opcoes[i]-1], calcularValor(valores[i], opcoes[i])) )
