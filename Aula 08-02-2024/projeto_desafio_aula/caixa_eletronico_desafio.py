# MENU
# 1 - Sacar
# 2 - Depositar
# 3 - Sair

# https://dontpad.com/516dfs
# prof.gabrielphilippe@gmail.com
# Abrir lista de Exercicios Python Google

# Importando o pacote do "os" o serviço chamado system
from os import system

controle = True

while controle:
    print(
        """
        CAIXA ELETRÔNICO - BANCO NACIONAL DO BRASIL (BNB)

        1 - Sacar
        2 - Sair

        """
    )

    opcao = input("Informe a opção desejada: ")

    match opcao:
        case "1":
            valor_saque = 0

            while valor_saque <= 0 or valor_saque > 1000:
                valor_saque = int(input("Informe o valor para saque (até R$ 1.000,00): "))
                
            #Logica das Notas
            
            #Para limpar a Tela
            input("Aperte Enter para continuar.")
            system("cls")
        case "2":
            controle = False
else:
    print("Terminal encerrado com sucesso.")


# valor = 657

# notas_100 = valor // 100
# valor = valor % 100

# notas_50 = valor // 50
# valor = valor % 50

# notas_20 = valor // 20
# valor = valor % 20

# notas_10 = valor // 10
# valor = valor % 10

# notas_2 = valor // 2
# valor = valor % 2

# notas_1 = valor // 1
# valor = valor % 1

# print(
#     f"""
#     Notas de R$ 100,00 {notas_100}
#     Notas de R$  50,00 {notas_50}
#     Notas de R$  20,00 {notas_20}
#     Notas de R$  10,00 {notas_10}
#     Notas de R$   2,00 {notas_2}
#     Notas de R$   1,00 {notas_1}
#     """
# )
    