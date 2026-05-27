quantidade = int(input())
numeros = []
for _ in range(quantidade):
    numero = input()
    numeros.append(numero)

resultado = numeros[1:quantidade]
resultado.append(numeros[0])
print(f'{" ".join(resultado)}')