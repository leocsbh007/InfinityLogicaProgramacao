
valor = 657

notas_100 = valor // 100
valor = valor % 100

notas_50 = valor // 50
valor = valor % 50

notas_20 = valor // 20
valor = valor % 20

notas_10 = valor // 10
valor = valor % 10

notas_2 = valor // 2
valor = valor % 2

notas_1 = valor // 1
valor = valor % 1

print(
    f"""
    Notas de R$ 100,00 {notas_100}
    Notas de R$  50,00 {notas_50}
    Notas de R$  20,00 {notas_20}
    Notas de R$  10,00 {notas_10}
    Notas de R$   2,00 {notas_2}
    Notas de R$   1,00 {notas_1}
    """
)
    