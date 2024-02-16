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
    while idade >= 0 or idade < 150:
        print("Idade invalida")
        idade = input("Digite sua idade: ")
    
    
    else:
        controle = False

else:
    print("Terminal encerrado com sucesso.")