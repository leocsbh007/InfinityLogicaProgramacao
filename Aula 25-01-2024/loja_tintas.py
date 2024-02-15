# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

print(10*'=-', 'Loja de Tintas',10*'=-')
area = float(input('Qual é o tamanho da area (m2): '))

cobertura = area / 3
lata = 18
preco = 80
if cobertura < 18:
    custo = preco
else:
    custo = preco * cobertura

print(cobertura)
print(custo)
