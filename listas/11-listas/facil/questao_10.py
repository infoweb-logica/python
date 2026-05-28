quantidade = int(input())
numeros = list(map(int, input().split()))
# numeros = [int(item) for item in input().split()]
numero = int(input())

ocorrencia = -1
for indice, item in enumerate(numeros):
    if numero == item:
        ocorrencia = indice

print(f'{ocorrencia}')