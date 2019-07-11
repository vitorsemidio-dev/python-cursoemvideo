"""
102
fatorial (num, show = False)

	Documentação
se show
	print n * (n-1) * ... * 1 = fatorial num
senão
	return fatorial num

"""

def fatorial (num, show=False):
    if show:
        if num == 1:
            print(f"{num}", end=" = ")
            return num
        print(f"{num}", end=" x ")
        return num * fatorial(num-1, show)

    if num == 1:
        return num
    return num * fatorial(num-1, show)

print(fatorial(5, True))