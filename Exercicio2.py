# 2. Faça um programa que leia 4 valores, calcule a média e 
# imprima positivo ou negativo (para ser posi-
# tivo a média deve ser acima de 1).

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

media = (n1 + n2 +  n3 + n4) / 4

if media >= 0:
    print("A média é",media,"Valor positivo!!")
else:
    print("A média é",media,"Valor negativo!!")
