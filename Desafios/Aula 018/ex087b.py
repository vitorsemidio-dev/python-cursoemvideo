"""
087
Aprimore o desafio anterior, mostrando no final:
a) a soma de todos os valores pares digitados.
b) a soma dos valores da terceira coluna.
c) o maior valor da segunda linha.
"""
from datetime import date
meses = {
	1:"Janeiro", 2:"Fevereiro", 3:"Marco", 4:"Abril", 5:"Maio", 6:"Junho",
	7:"Julho", 8:"Agosto", 9:"Setembro", 10:"Outubro", 11:"Novembro", 12:"Dezembro"
}

dia = date.today().day
mes = date.today().month
ano = date.today().year
data = f"{dia} de {meses[mes]} de {ano}"

print(data)
