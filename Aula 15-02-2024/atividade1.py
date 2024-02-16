# Crie um programa que, utilizando um loop for, encontre o
# primeiro número na sequência de 1 a 50 que seja divisível
# por 6 e pare a execução.


for num in range(1, 50+1):
    numero = num % 6
    if numero == 0:
        print(numero, num)
        break


