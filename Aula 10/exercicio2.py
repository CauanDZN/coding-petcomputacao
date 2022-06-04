def area(larg, comp):
    a = larg*comp
    print(f"A área de um terreno {larg}x{comp} é de {a}m²")


l = float(input("Qual a largura?: "))
c = float(input("Qual o comprimento?: "))
area(l, c)