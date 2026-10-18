# SETS são estruturas de dados que armazenam uma coleção de valores.
# Eles são criados usando chaves {} ou a função set().
#
# Características principais:
# - Não permitem valores repetidos.
# - Não possuem ordem fixa.
# - Não usam índices, então set[0] gera erro.
# - Podem ser alterados: é possível adicionar e remover elementos.
# - Aceitam tipos imutáveis, como números, textos e tuplas.
# - Não aceitam listas ou dicionários dentro deles.

# Criando sets
numeros = {1, 2, 3, 2, 1}
nomes = {"Julia", "Yago", "Lucas"}
set_vazio = set()  # {} cria um dicionário vazio, por isso usamos set()

print(numeros)       # {1, 2, 3}; os repetidos são removidos
print(type(numeros)) # <class 'set'>

# Sets não possuem posições fixas:
# print(numeros[0])  # ERRO: um set não pode ser acessado por índice

# Adicionando elementos
nomes.add("Ana")
print(nomes)

# Adicionando vários elementos
nomes.update(["Pedro", "Maria", "João"])
print(nomes)

# Removendo elementos
nomes.remove("Yago")      # remove; gera erro se o elemento não existir
nomes.discard("Carlos")   # remove se existir; não gera erro se não existir

# remove() retornaria erro caso o elemento não existisse:
# nomes.remove("Carlos")

print(nomes)

# Quantidade de elementos
print(len(nomes))

# Verificando se um elemento existe
if "Julia" in nomes:
    print("Julia está no set.")

# Percorrendo um set
for nome in nomes:
    print(nome)

# Convertendo lista em set para remover valores repetidos
lista_numeros = [1, 2, 2, 3, 4, 4, 5]
numeros_unicos = set(lista_numeros)

print(numeros_unicos)  # {1, 2, 3, 4, 5}

# Convertendo de volta para lista, caso precise usar posições/índices
lista_sem_repeticao = list(numeros_unicos)
print(lista_sem_repeticao)

# Operações entre sets
turma_a = {"Julia", "Yago", "Ana"}
turma_b = {"Yago", "Lucas", "Ana"}

# União: reúne todos os elementos, sem repetir
print(turma_a | turma_b)
print(turma_a.union(turma_b))

# Interseção: mostra os elementos presentes nos dois sets
print(turma_a & turma_b)
print(turma_a.intersection(turma_b))

# Diferença: mostra os elementos que estão apenas no primeiro set
print(turma_a - turma_b)
print(turma_a.difference(turma_b))

# Diferença simétrica: elementos que estão em apenas um dos sets
print(turma_a ^ turma_b)
print(turma_a.symmetric_difference(turma_b))

# Verificando relações entre sets
print(turma_a.issubset(turma_b))    # turma_a está totalmente dentro de turma_b?
print(turma_a.issuperset(turma_b))  # turma_a contém todos os dados de turma_b?
print(turma_a.isdisjoint(turma_b))  # não possuem nenhum elemento em comum?

# Limpando todos os elementos
copia_nomes = nomes.copy()  # cria uma cópia
nomes.clear()

print(nomes)        # set()
print(copia_nomes)  # mantém a cópia original