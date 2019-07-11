from termcolor import colored

papelaria = (
    "Lapis", 1.70,
    "Borracha", 0.5,
    "Estojo", 20.50,
    "Esquadro Metalico", 3.70
)


#print(f"\033[1;32m{'LISTA DE PREÇOS':=^44}\033[m")
print(f"\033[1;32m{'LISTA DE PREÇOS':=^44}")
for i in range(int(len(papelaria)/2)):
    item = papelaria[2*i]
    preco = papelaria[2*i+1]
    print(f"| \033[33m{item:.<30} R${preco:7.2f}", end=" \033[32m|\n")

print(colored("="*44, "green"))

