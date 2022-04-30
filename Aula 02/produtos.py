import os

os.system('cls')
numero_unidade_p1 = int(input("Insira o número de unidades do produto 1: "))
preco_da_unidade_p1 = int(input("Insira o preço da unidade do produto 1: "))

os.system('cls')
numero_unidade_p2 = int(input("Insira o número de unidades do produto 2: "))
preco_da_unidade_p2 = int(input("Insira o preço da unidade do produto 2: "))

os.system('cls')
total = numero_unidade_p1 * preco_da_unidade_p1 + numero_unidade_p2 * preco_da_unidade_p2
print("\nO total gasto é: R$", total)