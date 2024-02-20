# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

# x2 = x + x1
# x = x1
# x1 = x2
# 

num = int(input("Entre com o numero para gerar sua sequencia de Fibonacci: "))
x = 1
x1 = 1
x2 = 0
for i in range(1, num+1):
    print(x, end=" ") 
    x2 = x + x1
    x = x1
    x1 = x2
    
else:
    
    print("\nfim da sequencia")