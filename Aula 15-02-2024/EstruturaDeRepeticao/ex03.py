# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

from os import system
controle = True

while controle:
    
    print(
        """
        ENTRE COM AS INFORMAÇÕES ABAIXO

        # Nome: maior que 3 caracteres;
        # Idade: entre 0 e 150;
        # Salário: maior que zero;
        # Sexo: 'f' ou 'm';
        # Estado Civil: 's', 'c', 'v', 'd';
        
        """
    )
    
    nome = input("Digite seu nome: ")
    
    while len(nome) <= 3:
        print("Quantidade de caracteres Invalida!!")
        nome = input("Digite seu nome: ")    
    idade = input("Digite sua Idade: ")
    while int(idade) < 0 or int(idade) > 150:
        print("Idade invalida")
        idade = input("Digite sua idade: ")
    salario = input("Entre com o seu Salário: ")
    while int(salario) <= 0:
        print("Valor de Salário não aceito")
        salario = input("Entre com o seu Salário: ")
    sexo = input("Qual é o seu Sexo (f: Feminino - m: Masculino): ")
    while sexo not in ("fm"):
        print("Entrada invalida!")
        sexo = input("Qual é o seu Sexo (f: Feminino - m: Masculino): ")
    estado_civil = input("Esatado Civil (s - Solteiro(a), c - Casado(a), v - Viuvo(a), d - Divorciado(a)): ")
    while estado_civil not in ("scvd"):
        print("Entrada invalida!")
        estado_civil = input("Esatado Civil (s - Solteiro(a), c - Casado(a), v - Viuvo(a), d - Divorciado(a)): ")
    
    else:
        controle = False

    if sexo == "f":
        sexo = "f - Feminino"
    else:
        sexo = "m - Masculino"

    if estado_civil == "s":
        estado_civil = "s - Solteiro(a)"
    elif estado_civil == "c":
        estado_civil = "c - Casado(a)"
    elif estado_civil == "v":
        estado_civil = "v - Viuvo(a)"
    else:
        estado_civil = "d - Divorciado(a)"

    print(
        f"""
        VOCÊ DIGITOU AS INFORMAÇÕES ABAIXO

        # Nome: {nome}
        # Idade: {idade} anos
        # Salário: R${salario}
        # Sexo: {sexo}
        # Estado Civil: {estado_civil}
        
        """
    )

else:
    print("Terminal encerrado com sucesso.")