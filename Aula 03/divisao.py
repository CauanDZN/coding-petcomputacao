num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if num2 <= 0:
    print("Erro! O segundo número não pode ser menor ou igual a 0.")
else:
    div = num1 / num2
    print("O resultado da divisão de", num1, "e", num2, "é", div)