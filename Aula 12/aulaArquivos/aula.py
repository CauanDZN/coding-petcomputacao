arquivo = open('../aulaFun_parte2/texto.txt', encoding='utf-8').readlines();
'''n = int(input("Até qual linha você quer ler? "))
if n > len(arquivo):
    print('O n não pode ser maior que o número de linhas do arquivo')
else:
    for x in range(0, n):
        print(arquivo[x].rstrip())'''

'''for linha in arquivo:
    print(linha.rstrip())

n = int(input("Até qual linha você quer copiar? "))
arquivoDeCopia = open('arquivoCopia.txt', "w")
for x in range(0,n):
    arquivoDeCopia.write(arquivo[x])

arquivoDeCopia.close()'''

arquivo1 = open('arquivo1.txt', encoding='utf-8').read().split('\n')
arquivo2 = open('arquivo2.txt', encoding='utf-8').read().split('\n')
stringNova = ""
if len(arquivo1) != len(arquivo2):
    print("os arquivos precisam ter o mesmo número de linhas")
else:
    for x in range(len(arquivo1)):
        stringNova += arquivo1[x] + " " + arquivo2[x] + " "

print(stringNova)

'''boletimGeralDaTurma = open('Boletim.txt', "w")
i = 1
linha = ""
while i != '0':
    nomeDoAluno = input("digite o nome do aluno: ")
    notaDoAluno = input("Digite a nota do aluno: ")
    linha = nomeDoAluno + " - " + notaDoAluno + "\n"
    boletimGeralDaTurma.write(linha)
    i = input("Para parar digite '0': ")'''

'''boletimGeralDaTurma = open('Boletim.txt').read().split('\n')
numeroDeALunos = len(boletimGeralDaTurma)-1
soma = 0
for x in range(numeroDeALunos):
    nota = boletimGeralDaTurma[x].split(' - ')[1]
    soma += int(nota)

print(soma/numeroDeALunos)'''


    
