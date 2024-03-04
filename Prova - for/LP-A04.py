# [LP-A04] ENTREGUE SEU PROJETO ABAIXO SEGUINDO AS OBSERVAÇÕES

# SUGESTÃO DE PROJETO:

# SIMULADOR DE CADASTRO DE SENHA E INICIALIZAÇÃO DE CELULAR

# Utilizando o aprendizado desta aula, implementaremos um sistema de cadastro de senha e inicialização do celular utilizando o loop "for".

# Após ligar o celular, o usuário é solicitado a inserir a senha cadastrada.
# São permitidas 3 tentativas até que o telefone seja bloqueado.
# Se o usuário acertar a senha, uma mensagem de boas-vindas é exibida: "Bem-vindo."
# Se o usuário errar a senha, uma mensagem informando o erro é exibida, junto com o número de tentativas restantes até o bloqueio do telefone.
# Pense em todas as possibilidades e faça um sistema completo.

senha1 = "teste1"

senha = input("Insira a Senha cadastrada no celular: ")
for tentativas in range (1,4):
    #Verifica se é a senha Valida
    if senha == senha1:
        print("Bem-Vindo.")
        break
    # Vai para o erro de senhas
    else:
        # Verifica o numero de tentativas
        if tentativas < 3:
            print("São permitidas 3 tentativas")
            #Para exibir a mensagem no Singular
            if tentativas == 1:
                print(f"Você já errou {tentativas} vez")
            #Exibe um mensagem de Alerta para informar que já digitou duas vezes errado
            # e exibir a mensagem no plural
            elif tentativas == 2:                
                print(f"Você já errou {tentativas} vezes")
                print("Mais um erro e o celular será bloqueado")
            #Solicita novamente um senha ao Usuario            
            senha = input("Insira a Senha cadastrada no celular: ")
        # Estouro de tentativas de acesso ao celular
        else:
            print(f"Você já errou {tentativas} vezes")
            print("Telefone Bloqueado")
