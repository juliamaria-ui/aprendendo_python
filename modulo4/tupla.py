# Tuplas são estruturas de dados em Python que armazenam coleções de valores.
# Para criar uma tupla, usamos parênteses ().

valores = (1, 2, 3, 4, 5)
nomes = ("Yago", "Lucas", "José")
conjunto = (1, 2, "Yago", 3, "Julia")  # Tuplas podem ter diferentes tipos de dados

print(type(valores))  # imprime que é do tipo tuple
print(type(nomes))
print(conjunto)       # imprime todos os dados da tupla

# As posições começam em 0:
# 0=1, 1=2, 2=Yago, 3=3...

print(conjunto[0:3])  # imprime as posições 0, 1 e 2

print(conjunto[0])    # imprime o elemento da posição 0
print(conjunto[-1])   # imprime o último elemento da tupla

print(len(conjunto))  # mostra a quantidade de elementos

# Tuplas são imutáveis: não é possível alterar, adicionar ou remover itens.
# conjunto[0] = "Ana"       # ERRO
# conjunto.append("Maria")  # ERRO
# del conjunto[0]           # ERRO

# Métodos principais das tuplas:
numeros = (1, 2, 3, 2, 4, 2)

print(numeros.count(2))  # conta quantas vezes o número 2 aparece
print(numeros.index(3))  # mostra a posição onde o número 3 está

# Percorrendo cada elemento da tupla:
i = 0

while i < len(conjunto):
    print(f"posição: {i} | elemento: {conjunto[i]} | tipo: {type(conjunto[i])}")
    i += 1

# Também é possível percorrer com for:
for elemento in conjunto:
    print(elemento)

# Para criar uma tupla com apenas um item, é necessária uma vírgula:
item = ("Python",)
print(type(item))