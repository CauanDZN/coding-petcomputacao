lista = ["banana", "maçã", "manga", "abacate"]

#in: Verificar se um elemento está ou não na lista. Se estiver, retornar True. Caso contrário, retornar False.
print("banana" in lista) 
print("limão" in lista) 

#Método .insert(): inserir um elemento em um determinado índice da lista.
lista.insert(0, "romã") 

#Método append(): adicionar um elemento no final da lista.
lista.append("maracuja")

#Método extend(): extende a primeira lista com uma outra (junta as duas listas).
lista2 = ["cereja", "limão"]
lista.extend(lista2)

#Método remove(): remove um determinado elemento na lista.
lista.remove("banana")  

#Método pop(): remove e retorna um item de determinado índice na lista. Esse valor retornado pode
# ser usado para realizar outra ação posteriormente, caso seja necessário.
x = lista.pop(0) #removendo o valor no índice 0 da lista e guardando esse valor numa variável 'x'.

#del: Apenas remove um item de determinado índice na lista.
del lista[0] 

#Exemplo: removendo um elemento de uma lista usando o pop e adicionando esse elemento em uma
# outra lista

lista2 = []
lista2.append(lista.pop(1))
print(lista) #printando lista anterior, agora com um valor removido
print(lista2) #printando a outra lista, agora com um valor adicionado

#Método clear(): limpa a lista, deixando-a vazia.
lista.clear() 
print(lista) 

#Função len(): retorna o número de elementos da lista (tamanho)
lista = ["banana", "maçã", "manga", "abacate"]
tamanho = len(lista)
print(tamanho)

#for x in lista: percorrer todos os elementos da lista. 
#Exemplo: percorrendo todos os elementos da lista e printando-os
lista = [1, 3, 5, 7, 9]
for x in lista:
    print(x)

#for i in range(len(lista)): outra forma de percorrer os elementos da lista, agora utilizando os
#índices   
for i in range(len(lista)):
    print(lista[i])

#percorrendo e printando só os índices pares (0, 2, 4, ...)
lista = ["banana", "maça", "limão", "cereja", "abacate"]
for i in range(len(lista)):
    if i%2 == 0:
        print(lista[i])

#Percorrendo toda a lista e printando os elementos utilizando
#o while 
i = 0
while i < len(lista):
    print(lista[i])
    i+=1

#exercício 1: Faça um programa para receber números naturais do usuário e colocá-los em uma lista.
#  Os números deverão ser recebidos até o usuário digitar -1. Após isso, receba um número N do
#  usuário e verifique se ele está presente na lista. Se estiver, escreva que o número está
#  presente. Caso não esteja, escreva que ele não está presente.
x = 0
lista = []
while x != -1:
    x = int(input("Insira um número natural: "))
    if x != -1:
        lista.append(x)

N = int(input("Insira um número N para verificar: "))

if N in lista:
    print("O elemento ", N, "está na lista")
else:
    print("O elemento ", N, "não está na lista")

#exercício 2: Faça um programa para receber números naturais do usuário e colocá-los em uma lista.
#  Os números deverão ser recebidos até o usuário digitar -1. Após isso, receba um número N do 
# usuário e verifique se ele está presente na lista. Se estiver, remova o elemento da lista. Caso
#  não esteja, escreva que ele não está presente. Além disso, escreva a lista no final.
x = 0
lista = []
while x != -1:
    x = int(input("Insira um número natural: "))
    if x != -1:
        lista.append(x)

print("Lista: ", lista)

N = int(input("Insira um número N para remover: "))

if N in lista:
    while (N in lista):    
        lista.remove(N)
else:
    print("O elemento ", N, "não está na lista")

print("Lista: ", lista)


#exercício 3: Faça um programa para inverter que recebe um número de qualquer tamanho e retorna o
#  inverso dele (algarismos).
n = input("Insira um número: ")
novo_n = ''
for i in range(len(n)-1, -1, -1):
    novo_n += n[i]
print(novo_n)

#exercício 4: Faça um programa que calcule a sequência de fibonacci até um número N fornecido pelo usuário. 
N = int(input("Insira o número limite: "))

lista = [0,1]
i = 0
while lista[i] + lista[i+1] <= N:
    lista.append(lista[i] + lista[i+1])
    i+=1

print(lista)






    











