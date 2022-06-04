nomeDoCliente = "Rafael"
divida = float(input("Digite o valor da dívida em dólares: "))

def valorEmReais(cliente, valorDivida):
    valorDaDividaEmReais = valorDivida*5
    print(f'O valor a ser pago em reais pelo cliente {cliente} é {valorDaDividaEmReais}')

valorEmReais(nomeDoCliente, divida)