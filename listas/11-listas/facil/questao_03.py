# Exemplo de entrada
# 7
# 2 
# 5 
# 8 
# 11 
# 14 
# 7 
# 20
quantidade = int(input())
numeros = []
pares = 0
for _ in range(quantidade):
    numero = int(input())
    numeros.append(numero)
    if numero % 2 == 0:
        pares += 1

# exmeplo de saída
# 4
# as saídas prefira com fstring
print(f'{pares}')