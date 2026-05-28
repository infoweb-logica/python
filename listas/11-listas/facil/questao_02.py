# Exxemplo de entrada
# 6
# 8
# 2 
# 10 
# -3 
# 7 
# 4
### primeira versão
# quantidade = int(input())
# numeros = []
# for _ in range(quantidade):
#     numero = int(input())
#     numeros.append(numero)

# menor = -999999999
# maior = 999999999
# for numero in numeros:
#     if menor > numero:
#         menor = numero
#     if maior < numero:
#         maior = numero

### segunda versão
quantidade = int(input())
numeros = []
menor = 999999999
maior = -999999999
for _ in range(quantidade):
    numero = int(input())
    numeros.append(numero)
    if menor > numero:
        menor = numero
    if maior < numero:
        maior = numero

# exmeplo de saída
# -3 10
# as saídas prefira com fstring
print(f'{menor} {maior}')