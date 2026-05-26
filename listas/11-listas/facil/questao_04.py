quantidade = int(input())
numeros = []
soma = 0
for _ in range(quantidade):
    numero = int(input())
    numeros.append(numero)
    soma += numero

media = soma / quantidade
contador = 0
for numero in numeros:
    if numero > media:
        contador += 1
print(f'{contador}')