quantidade = int(input())
numeros = list(map(int, input().split()))
# numeros = [int(item) for item in input().split()]
numero = int(input())

ocorrencia = 0
for indice, item in enumerate(numeros):
    if numero == item:
        ocorrencia += 1

print(f'{ocorrencia}')