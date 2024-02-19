# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento

#Juros compostos
# #M = C (1 + i)**t
# "Capital (C): é o primeiro valor investido. Conhecemos como capital o valor inicial da negociação, ou seja, ele é o valor de referência para calcularmos os juros com o passar do tempo.
# Juros (J): é o valor de compensação para o rendimento. Quando uma instituição financeira faz um empréstimo, ela está abdicando-se de estar com esse dinheiro em um determinado prazo, porém, quando ela for recebê-lo, seu valor será corrigido pelo que chamamos de juros, e é com base nele que a empresa vê uma compensação pelo empréstimo. Em um investimento, trata-se do valor dos rendimentos adquiridos.
# Taxa de juros (i): é a porcentagem cobrada em cima do capital a cada instante. Essa taxa pode ser ao dia (a.d.), ao mês (a.m.), ao bimestre (a.b.) ou ao ano (a.a.). A taxa de juros é uma porcentagem geralmente representada na forma percentual, porém, para calcular-se o juros composto, é importante escrevê-la sempre na forma decimal.
# Tempo (t): é o tempo em que o capital ficará aplicado. É importante que a taxa de juros (i) e o tempo (t) estejam sempre na mesma unidade de medida.
# Montante (M): é o valor final da transação. O montante é calculado pela soma do capital com os juros — M = C + J.

controle = True
ano = 1
mes = 1
count = 0

pop_paisA = 80000
taxa_paisA = 0.03 # Taxa ao ano
taxa_paisA_mes = 0.03/12 # Taxa ao mês
#montante_paisA = pop_paisA * ((1 + taxa_paisA_mes)**mes)

pop_paisB = 200000
taxa_paisB = 0.015 # Taxa ao ano
taxa_paisB_mes = 0.015/12 # Taxa ao mes
#montante_paisB = pop_paisB * ((1 + taxa_paisB_mes)**mes)

#difmontante = montante_paisB/montante_paisA

#print("%.2f"%montante_paisA, "%.2f"%montante_paisB)
#print("%.2f"%difmontante)
#print(ano)
#print("%.2f"%(mes/12))

#difmontante = montante_paisB/montante_paisA

while controle:    
    montante_paisA = pop_paisA * ((1 + taxa_paisA)**ano) 
    montante_paisB = pop_paisB * ((1 + taxa_paisB)**ano)
    difmontante = montante_paisB/montante_paisA

    #ano += 1
    #mes +=1
    if montante_paisA >= montante_paisB:
        controle = False
    else: 
        ano += 1

else:
    #print("%.2f"%montante_paisA, "%.2f"%montante_paisB)
    #print("%.2f"%difmontante)
    print(f"Serão necessários {ano} anos")
    montante_paisA = "%.0f"%montante_paisA
    montante_paisB = "%.0f"%montante_paisB
    print(f"A população do Pais A será de {montante_paisA} habitantes")
    print(f"A população do Pais B será de {montante_paisB} habitantes")
    #print(mes//12)
    #print(mes%12)
    print("Laço terminou!!!")

