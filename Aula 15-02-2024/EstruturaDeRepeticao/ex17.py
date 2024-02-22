# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input("Digite um numero para encontra o Fatorial: "))
fatorial = num
for i in range(1, num):    
    fatorial = fatorial * i
    print(num, i, fatorial)

else: 
    print(f"O fatorial de {num} = {fatorial}")