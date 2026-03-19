# Notas de aula de Python

## Informações gerais

- **Público alvo**: alunos da disciplina de **Introdução a lógica e programação** do curso de [Infoweb (Técnico Integrado em Informática para Internet)](https://diatinf.ifrn.edu.br/cursos/tecnico-em-informatica-para-internet/) na [DIATINF (Diretoria Acadêmica de Gestão e Tecnologia da Informação)](https://diatinf.ifrn.edu.br/) no [CNAT-IFRN (Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte - Campus Natal-Central)](https://portal.ifrn.edu.br/campus/natalcentral/)

## Notas de aula

1. Introdução
2. Variáveis e operadores aritiméticos
3. FIXME

## Resumo da Sintaxe em Python

### 1. Variáveis e Tipos de Dados

```python
# Inteiro
idade = 25

# Ponto flutuante
altura = 1.75

# String
nome = "Maria"

# Booleano
ativo = True

# NoneType
valor = None
```

---

### 2. Operadores

```python
# Aritméticos
soma = 10 + 3       # 13
subtracao = 10 - 3  # 7
produto = 10 * 3    # 30
divisao = 10 / 3    # 3.333...
div_inteira = 10 // 3  # 3
modulo = 10 % 3     # 1
potencia = 2 ** 8   # 256

# Comparação
10 == 10   # True
10 != 5    # True
10 > 5     # True
10 < 5     # False
10 >= 10   # True
10 <= 9    # False

# Lógicos
True and False  # False
True or False   # True
not True        # False
```

---

### 3. Strings

```python
texto = "Olá, mundo!"

# Comprimento
len(texto)          # 11

# Maiúsculas / minúsculas
texto.upper()       # "OLÁ, MUNDO!"
texto.lower()       # "olá, mundo!"

# Fatiamento (slicing)
texto[0:3]          # "Olá"
texto[-6:]          # "mundo!"

# Formatação (f-string)
nome = "Ana"
print(f"Bem-vinda, {nome}!")  # Bem-vinda, Ana!

# Concatenação
saudacao = "Olá" + ", " + "mundo!"
```

---

### 4. Listas

```python
frutas = ["maçã", "banana", "laranja"]

frutas[0]           # "maçã"
frutas[-1]          # "laranja"

frutas.append("uva")       # adiciona ao final
frutas.remove("banana")    # remove pelo valor
frutas.pop(0)              # remove pelo índice

len(frutas)         # quantidade de elementos

# Iteração
for fruta in frutas:
    print(fruta)
```

---

### 5. Tuplas

```python
# Imutáveis (não podem ser alteradas após criadas)
coordenadas = (10.5, 20.3)

x = coordenadas[0]  # 10.5
y = coordenadas[1]  # 20.3
```

---

### 6. Dicionários

```python
pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "cidade": "São Paulo"
}

pessoa["nome"]                  # "Carlos"
pessoa["idade"] = 31            # atualiza valor
pessoa["profissao"] = "Dev"     # adiciona nova chave

# Iteração
for chave, valor in pessoa.items():
    print(chave, ":", valor)
```

---

### 7. Conjuntos (Sets)

```python
numeros = {1, 2, 3, 4, 4, 5}  # {1, 2, 3, 4, 5} — sem duplicatas

numeros.add(6)
numeros.discard(3)

# Operações de conjuntos
a = {1, 2, 3}
b = {3, 4, 5}
a | b   # união:       {1, 2, 3, 4, 5}
a & b   # interseção:  {3}
a - b   # diferença:   {1, 2}
```

---

### 8. Estruturas de Controle

#### Condicional

```python
nota = 7

if nota >= 9:
    print("Ótimo")
elif nota >= 6:
    print("Bom")
else:
    print("Insuficiente")
```

#### Laço `for`

```python
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4

for letra in "Python":
    print(letra)
```

#### Laço `while`

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

#### `break` e `continue`

```python
for i in range(10):
    if i == 3:
        continue   # pula o 3
    if i == 7:
        break      # encerra no 7
    print(i)
```

---

### 9. Funções

```python
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Pedro"))   # Olá, Pedro!

# Parâmetro padrão
def potencia(base, expoente=2):
    return base ** expoente

potencia(3)     # 9
potencia(3, 3)  # 27

# Múltiplos retornos
def min_max(lista):
    return min(lista), max(lista)

minimo, maximo = min_max([4, 1, 7, 2])
```

---

### 10. Funções Lambda

```python
dobrar = lambda x: x * 2
dobrar(5)   # 10

# Com map e filter
numeros = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x * 2, numeros))  # [2, 4, 6, 8, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))  # [2, 4]
```

---

### 11. Classes e Objetos

```python
class Animal:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som

    def falar(self):
        print(f"{self.nome} faz '{self.som}'")

# Herança
class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Au au")

    def buscar(self):
        print(f"{self.nome} foi buscar a bolinha!")

rex = Cachorro("Rex")
rex.falar()    # Rex faz 'Au au'
rex.buscar()   # Rex foi buscar a bolinha!
```

---

### 12. Tratamento de Exceções

```python
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Erro: {e}")
except (TypeError, ValueError) as e:
    print(f"Erro de tipo ou valor: {e}")
else:
    print("Sem erros!")
finally:
    print("Bloco finally sempre executa")
```

---

### 13. Compreensão de Listas

```python
# Lista com quadrados de 0 a 9
quadrados = [x ** 2 for x in range(10)]

# Com condição
pares = [x for x in range(20) if x % 2 == 0]

# Dicionário por compreensão
quadrados_dict = {x: x ** 2 for x in range(5)}
```

---

### 14. Módulos e Importações

```python
import math
print(math.sqrt(16))   # 4.0
print(math.pi)         # 3.14159...

from datetime import datetime
agora = datetime.now()
print(agora)

# Apelido (alias)
import numpy as np
```

---

### 15. Leitura e Escrita de Arquivos

```python
# Escrita
with open("arquivo.txt", "w", encoding="utf-8") as f:
    f.write("Olá, arquivo!\n")

# Leitura
with open("arquivo.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)

# Leitura linha a linha
with open("arquivo.txt", "r", encoding="utf-8") as f:
    for linha in f:
        print(linha.strip())
```

