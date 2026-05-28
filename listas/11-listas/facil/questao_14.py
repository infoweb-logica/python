quantidade = int(input())
numeros = []
resultado = []
for _ in range(quantidade):
    numero = int(input())
    numeros.append( numero )
    if numero % 2 == 0:
        resultado.append(str(numero * 2))
    else:
        resultado.append(str(numero))

print(f'{" ".join(resultado)}')