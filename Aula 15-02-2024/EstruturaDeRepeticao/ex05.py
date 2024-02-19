# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento
# Altere o programa ex04 permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.


controle = True
ano = 1
menu = ""

pop_paisA = 80000
taxa_paisA = 0.03 # Taxa ao ano

pop_paisB = 200000
taxa_paisB = 0.015 # Taxa ao ano


while menu != "S":    

    print(
        """
        Calculo de cresciomento populacional  
        Comparação entre taxas de crecimento

        # População Menor:
        # Taxa de Crescimento Anual (%): 
        # População Maior:
        # Taxa de Crescimento Anual (%);

        # S - Sair
                
        """
    )

    pop_paisA = input("Entre com o numero de habitantes população Menor (POPULAÇÃO - A): ")
    pop_paisB = input("Entre com o numero de habitantes população Menor (POPULAÇÃO - B): ")

    while int(pop_paisA) > int(pop_paisB):
        print("A população A deve ser menor que a População B")
        pop_paisA = input("Entre com o numero de habitantes população Menor (POPULAÇÃO - A): ")
        pop_paisB = input("Entre com o numero de habitantes população Menor (POPULAÇÃO - B): ")

    taxa_paisA = float(input("Entre com a Taxa de Crescimento da POPULAÇÃO - A: "))/100
    taxa_paisB = float(input("Entre com a Taxa de Crescimento da POPULAÇÃO - B: "))/100

    while taxa_paisA < taxa_paisB:
        print("A taxa de crescimento da População A deve ser menor que a Taxa de Crescimento da População B")
        taxa_paisA = input("Entre com a Taxa de Crescimento da POPULAÇÃO - A: ")
        taxa_paisB = input("Entre com a Taxa de Crescimento da POPULAÇÃO - B: ")

    while controle:
        montante_paisA = int(pop_paisA) * ((1 + taxa_paisA)**ano) 
        montante_paisB = int(pop_paisB) * ((1 + taxa_paisB)**ano)
        #difmontante = montante_paisB/montante_paisA
        #ano += 1

        if montante_paisA >= montante_paisB:
            controle = False
        else: 
            ano += 1

    else:
        print(f"Serão necessários {ano} anos")
        montante_paisA = "%.0f"%montante_paisA
        montante_paisB = "%.0f"%montante_paisB
        print(f"A população do Pais A será de {montante_paisA} habitantes")
        print(f"A população do Pais B será de {montante_paisB} habitantes")
        ano = 1
        menu = input("Digite S para sair ou Enter para continuar: ")
        menu = menu.upper()
     
else:
    print("Laço terminou!!!")