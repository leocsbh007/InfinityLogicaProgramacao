# Faça um programa que leia 5 números e informe o maior número.

num = list()

for i in range (1,6):
    num.append(input(f"Entre com o {i}º numero: "))

print(max(num))