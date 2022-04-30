import os

os.system('cls')
salario_fixo = float(input("Insira o salario: R$"))

vendas_efetuadas = float(input("Insira o total de vendas do vendedor: R$"))

salario_total = (0.15 * vendas_efetuadas) + salario_fixo

print("Salario total: R$", salario_total)

print("\nYasser, Rafael, Thiago, Gabriel e Havillon são os melhores tutores que ja vi! ")