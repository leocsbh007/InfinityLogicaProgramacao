# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

# x2 = x + x1
# x = x1
# x1 = x2
# 
num = 5000
x = 1
x1 = 1
x2 = 0
# repete a té encontrar o numero que é maior que 500
while x < num:    
    print(x, end=" ") 
    x2 = x + x1
    x = x1
    x1 = x2
    
else:
    # Imprime mais um numero, pois ele será o primeiro maior que 500
    print(x, end=" ") 
    x2 = x + x1
    x = x1
    x1 = x2
    print("\nfim da sequencia")