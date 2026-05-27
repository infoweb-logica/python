quantidade = int(input())
numeros = []
for _ in range(quantidade):
    numero = input()
    numeros.append(numero)

resultado = numeros[0:quantidade-1]
resultado.insert(0, numeros[quantidade-1])
print(f'{" ".join(resultado)}')