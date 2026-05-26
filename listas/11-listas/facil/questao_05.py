quantidade = int(input())
numeros = []
for _ in range(quantidade):
    numero = int(input())
    numeros.append(numero)

inverso = [str(numero) for numero in numeros[::-1]]
print(f'{" ".join(inverso)}')