"""
063
Ler n e mostrar os n primeiros termos da Sequencia de Fibonacci.
"""
def fibonacci(fib):
    if fib == 0:
        return fib
    if fib == 1:
        return fib
    return fibonacci(fib-2) + fibonacci(fib-1)

n = int(input("Digite a quantidade de termos de Fibonacci que deseja ver: "))

for i in range(n):
    print("{}".format(fibonacci(i)), end=" ")