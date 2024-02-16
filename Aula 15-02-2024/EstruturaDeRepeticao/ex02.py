# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

from os import system
controle = True
while controle:
    print(
        """
        DIGITE O NOME DE USUARIO E SENHA

        SENHA DEVE SER DIFERENTE DE NOME DE USUARIO
        """
    )
    usuario = input("Digite seu Usuario: ")
    senha = input("Digite sua senha: ")
    
    if usuario != senha:
        print("Acesso permitido ao sistema")
        controle = False
    else:
        input("Nome de Usuario e Senha devem ser diferentes.  Digite ENTER para continuar!!!")
        system("cls")
        
else:
    print("Terminal encerrado com sucesso.")
    