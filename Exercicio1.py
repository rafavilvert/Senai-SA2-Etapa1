# 1. Dada a lista L = [5, 7, 2, 9, 4, 1, 3], 
# escreva um programa que imprima as seguintes informações:

L = [5, 7, 2, 9, 4, 1, 3]

# a) tamanho da lista;
print("O tamanho da lista é: %i elementos" % (len(L)))

# a) tamanho da lista de outra maneira
for i in L:
    tamanhoLista = L.index(i) + 1

print("O tamanho da lista é: ", tamanhoLista, "Elementos")

# b) maior valor da lista;
print("O maior valor da lista é: %i" % (max(L)))

# b) maior valor da lista de outra maneira
valorMaisAlto = -1
for i in L:
    recebeValor = i
    if (recebeValor > valorMaisAlto):
        valorMaisAlto = recebeValor
print("O valor mais alto é: ", valorMaisAlto)

# c) menor valor da lista;
print("O menor valor da lista é: %i" % (min(L)))

# c) menor valor da lista de outra maneira
menorvalor = 100
for i in L:
    recebeValor = i
    if (recebeValor < menorvalor):
        menorvalor = recebeValor
print("O valor mais alto é: ", menorvalor)

# d) soma de todos os elementos da lista;
print("A soma de todos os elementos da lista é: %i" % (sum(L)))

# d) soma de todos os elementos da lista de outra maneira
somaTotal = 0
for i in L:
    somaTotal = somaTotal + i
    
print("A soma de todos os elementos da lista é: ", somaTotal)

# e) lista em ordem crescente;
print("A orden crescente da lista é: ", end="")
print(sorted(L))

# e) lista em ordem crescente de outra maneira
def bubbleSort(L):
    for passnum in range(len(L)-1,0,-1):
        for i in range(passnum):
            if L[i]>L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp


bubbleSort(L)
print("A orden crescente da lista é: ", end="")
print(L)

# f) lista em ordem decrescente.
print("A orden decrescente da lista é: ", end="")
print(sorted(L, reverse=True))

# f) lista em ordem decrescente de outra maneira
def bubbleSort(L):
    for passnum in range(len(L)-1,0,-1):
        for i in range(passnum):
            if L[i]<L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp


bubbleSort(L)
print("A orden decrescente da lista é: ", end="")
print(L)
