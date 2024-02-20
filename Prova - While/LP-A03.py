# [LP-A03] Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). 
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

num = ""
count = 0
soma = 0
media = 0
while num != "0":
    # Recebe os numeros digitados no teclado
    num = input("Digite um numero: ")
    # Apenas valida se o numero for diferente de 0
    if num != "0":
        # Atualiza a contagem de numero digitados
        count += 1 
        # Faz a soma dos numeros
        soma = soma + int(num)


else:
    print(f"Você digitou {count} numeros")
    print(f"A soma dos números digitados é {soma}")
    # Calcula a media dos numeros
    media = soma / (count)
    print(f"A media aritimética dos numeros digitados é {media}")