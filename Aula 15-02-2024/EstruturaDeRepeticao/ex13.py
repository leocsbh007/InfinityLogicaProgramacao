# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

num = int(input("Entre com o numero: "))
expoente = int(input("Entre com o expoente: "))
resultado = 0

resultado = num
for i in range(1, expoente):
    resultado = resultado * num
    

print(f"O numero {num} elevado a {expoente} = {resultado}")