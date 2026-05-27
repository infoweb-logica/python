quantidade = int(input())
numeros = list(map(int, input().split()))
# numeros = [int(item) for item in input().split()]
numero = int(input())

resultado = "NAO"
for item in numeros:
    if numero == item:
        resultado = "SIM"
        break
print(f'{resultado}')