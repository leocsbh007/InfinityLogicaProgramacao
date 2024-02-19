# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input("Entre com o 1º numero: "))
num2 = int(input("Entre com o 2º numero: "))

for i in range (num1, num2+1):
    if i != num1 and i !=num2:
        print(i)