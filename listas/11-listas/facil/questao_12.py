quantidade = int(input())
numeros = list(map(int, input().split()))

resultado = []
for numero in numeros:
    numero_oposto = numero * -1
    resultado.append( str(numero_oposto) )
print(f'{" ".join(resultado)}')