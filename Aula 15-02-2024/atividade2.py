# Utilize um loop for para imprimir os números de 1 a 20,
# pulando os múltiplos de 3.

for num in range(1,20+1):
    numero = num % 3
    if numero != 0:
        print(num)