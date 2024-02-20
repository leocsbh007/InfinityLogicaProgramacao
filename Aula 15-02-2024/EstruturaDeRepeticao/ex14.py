# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

num = int(input("Digite um numero: "))
par = 0
impar = 0

for i in range(1,num+1):
    print(i, num)
    if i % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Numeros pares = {par}, Numeros impares = {impar}")