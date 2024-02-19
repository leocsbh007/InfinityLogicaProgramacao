# Faça um programa que leia 5 números e informe a soma e a média dos números.

num = list()
for i in range (1, 6):
    num.append(int(input(f"Informe o {i}º numero: ")))

soma = sum(num)
media = soma/int(len(num))
print(f"A soma é igual a {soma}")
print(f"A media é igual a {media}")