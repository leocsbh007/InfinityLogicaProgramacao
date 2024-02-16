# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# Importando o pacote do "os" o serviço chamado system
from os import system

controle = True

while controle:
    print(
        """
        ENTRE COM O VALOR DA NOTA

        Aceita apenas valores de 0 a 10
        
        """
    )

    opcao = input("Informe a opção desejada: ")

    if int(opcao) > 10:
            input("Valor invalido - Aperte Enter para continuar.")
            system("cls")
    else: 
        controle = False
else:
    print("Terminal encerrado com sucesso.")