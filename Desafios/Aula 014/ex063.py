"""
063
Sequencia de Fibonacci.
"""
from random import randint

def fibonacci(fib):
    if fib == 0:
        return fib
    if fib == 1:
        return fib
    return fibonacci(fib-2) + fibonacci(fib-1)



numeros = []
for i in range(randint(3, 15)):
    numeros.append(randint(0, 20))

for i in range(len(numeros)):
    print("Fib({}) = {}".format(numeros[i], fibonacci(numeros[i])))


