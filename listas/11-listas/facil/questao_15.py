def numero_existe_na_lista(numero, lista):
    # return lista.count(numero) != 0
    for item in lista:
        if numero == item:
            return True
    return False

quantidade = int(input())
numeros = list(map(int, input().split()))

resultado = []
for item in numeros:
    numero = str(item)
    nao_existe = not numero_existe_na_lista(numero, resultado)
    if nao_existe:
        resultado.append(numero)

print(f'{" ".join(resultado)}')

