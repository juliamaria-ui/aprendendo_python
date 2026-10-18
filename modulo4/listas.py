# Listas são estruturas de dados em Python que permitem armazenar
# uma coleção de elementos ou valores.
# Para criar uma lista, usamos colchetes [].

valores = [1, 2, 3, 4, 5]
nomes = ["Yago", "Lucas", "José"]
conjunto = [1, 2, "Yago", 3, "Julia"]  # É possível adicionar diferentes tipos de dados

print(type(valores))  # imprime que é do tipo list
print(type(nomes))
print(conjunto)       # imprime todos os dados da lista

# As posições começam em 0:
# 0 = 1, 1 = 2, 2 = "Yago", 3 = 3...

print(conjunto[0:3])  # imprime as posições 0, 1 e 2

conjunto[0] = "Ana"  # substitui o dado na posição 0 pela string "Ana"

nomes.append(5)      # adiciona o número 5 à lista nomes
del nomes[0]         # remove o nome na posição 0

print(len(conjunto))  # mostra o tamanho da lista

# Percorre a lista mostrando posição, elemento e tipo de dado
i = 0

while i <= len(conjunto) - 1:
    print(f"posição: {i} | elemento: {conjunto[i]} | tipo: {type(conjunto[i])}")
    i = i + 1