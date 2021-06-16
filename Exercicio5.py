# 5. Crie uma função que receba como parâmetro uma lista,
# com valores de qualquer tipo. A função deve
# imprimir todos os elementos da lista, enumerando-os.

lista = ["Nome", "Rafael", "Idade", 30, "Endereço", 105, "Media", 9.9]

def imprimir_lista(lista):
    for i in lista:
        print("O elemento", lista.index(i)+1, "é: ", end="")
        print(i)

imprimir_lista(lista)
