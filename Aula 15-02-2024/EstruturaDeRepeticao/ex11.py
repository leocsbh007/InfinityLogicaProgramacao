# Faça um programa que receba dois números inteiros e gere a soma dos números inteiros que estão no intervalo compreendido por eles.

num1 = int(input("Entre com o 1º numero: "))
num2 = int(input("Entre com o 2º numero: "))
soma = 0
for i in range (num1, num2+1):
    if i != num1 and i !=num2:
        soma = soma + i
        
            
    
print(soma)