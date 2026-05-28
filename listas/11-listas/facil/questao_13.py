quantidade = int(input())
numeros = list(map(int, input().split()))

resultado = []
for item in numeros:
    numero = item
    if numero < 0:
        numero = numero * -1
    resultado.append( str(numero) )
print(f'{" ".join(resultado)}')