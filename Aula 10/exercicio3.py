def voto(idade):
    if (idade < 16):
        print("VOTO NEGADO")
    elif ((idade >= 16 and idade < 18) or (idade > 70)):
        print("VOTO OPCIONAL")
    else:
        print("VOTO OBRIGATÓRIO")

voto(15)