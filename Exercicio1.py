# 1. Dada a lista L = [5, 7, 2, 9, 4, 1, 3], 
# escreva um programa que imprima as seguintes informações:

L = [5, 7, 2, 9, 4, 1, 3]

# a) tamanho da lista;
print("O tamanho da lista é: %i elementos" % (len(L)))

# b) maior valor da lista;
print("O maior valor da lista é: %i" % (max(L)))

# c) menor valor da lista;
print("O menor valor da lista é: %i" % (min(L)))

# d) soma de todos os elementos da lista;
print("A soma de todos os elementos da lista é: %i" % (sum(L)))

# e) lista em ordem crescente;
print("A orden crescente da lista é: ", end="")
print(sorted(L))

# f) lista em ordem decrescente.
print("A orden decrescente da lista é: ", end="")
print(sorted(L, reverse=True))
