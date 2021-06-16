# 3. Escreva um programa que leia 20 valores inteiros
# e informe a média deles, o maior e o menor valor.

lista = []
i = 0

while i < 20:
    L = int(input("Digite o valor %i° valor inteiro: " % (i+1)))
    lista.append(L)
    print(list)
    i += 1

print(lista)

media = sum(lista) / len(lista)
print("A media dos 20 números é %.2f" % (media))

print("O maior valor da lista é: %i" % (max(lista)))

print("O menor valor da lista é: %i" % (min(lista)))
