# 5
quantidade = int(input())

# receber varios numeros numa linha
# exemplo
#  3 1 4 1 5
entrada = input()       # "3 1 4 1 5"
lista = entrada.split() # ["3", "1", "4", "1", '5"]
numeros = [int(item) for item in lista] # [3, 1, 4, 1, 5]
# numeros = [int(item) for item in input().split()] # [3, 1, 4, 1, 5]

soma = 0
for numero in numeros:
    soma += numero
print(soma)

# print( sum(numeros) )