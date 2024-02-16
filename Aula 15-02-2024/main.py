valor = 979

notas = [200, 100, 50, 20, 10, 5, 2, 1]
qntd_notas = []

for nota in notas:
    qntd_notas.append(valor // nota)
    valor = valor % nota

print(30*"=-")
print("Usando Enumerate e FOR")
for indice, nota in enumerate(notas):
    if qntd_notas[indice] != 0:
        print(f"{qntd_notas[indice]} de R$ {nota},00")
        
print(30*"=-")
print("Usando indice e WHILE")
indice = 0
while indice < len(notas):
    if qntd_notas[indice] != 0:
        print(f"{qntd_notas[indice]} de R$ {notas[indice]},00")
    indice += 1

print(30*"=-")