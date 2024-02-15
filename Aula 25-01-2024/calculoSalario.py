# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

print(10*'=-','Calculo de INSS',10*'=-')

salario_hora = int(input('Quanto você ganha por hora: '))
hora_mes = int(input('Quantas horas você trabalha por mês '))

# Calcula o valor dop salario Bruto no mês
salario_bruto = float(salario_hora * hora_mes)
# Calcula o IR
ir = salario_bruto * 0.11
# calcula o inss
inss = salario_bruto * 0.08
# Calcula o desconto de sindicato
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (ir+inss+sindicato)
print(' + Salário Bruto : R$ ',"%.2f"% salario_bruto , '\n',
'- IR (11%) : R$ ', "%.2f"% ir , '\n',
'- INSS (8%) : R$ ', "%.2f"%inss , '\n',
'- Sindicato (5%) : R$ ', "%.2f"%sindicato , '\n'
' = Salário Liquido : R$ ', "%.2f"%salario_liquido)
print(20*'=-')

