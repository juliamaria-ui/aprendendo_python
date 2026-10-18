# Dicionários são estruturas de dados que armazenam informações
# no formato: chave : valor
# Eles são criados usando chaves {}.

pessoa = {
    "nome": "Julia",
    "idade": 20,
    "cidade": "São Paulo",
    "estudante": True
}

print(type(pessoa))  # imprime <class 'dict'>
print(pessoa)        # imprime todo o dicionário

# Acessando valores pela chave
print(pessoa["nome"])
print(pessoa["idade"])

# get() também acessa um valor.
# É mais seguro, pois não gera erro se a chave não existir.
print(pessoa.get("cidade"))
print(pessoa.get("telefone", "Não informado"))

# Alterando um valor existente
pessoa["idade"] = 21

# Adicionando uma nova chave e valor
pessoa["telefone"] = "11999999999"

print(pessoa)

# Removendo dados
del pessoa["cidade"]       # remove pela chave
pessoa.pop("telefone")     # remove e retorna o valor removido

print(pessoa)

# Principais métodos para visualizar o dicionário
print(pessoa.keys())    # mostra apenas as chaves
print(pessoa.values())  # mostra apenas os valores
print(pessoa.items())   # mostra chave e valor juntos

# Verificando se uma chave existe
if "nome" in pessoa:
    print("A chave nome existe.")

# Percorrendo somente as chaves
for chave in pessoa:
    print(chave)

# Percorrendo chaves e valores
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# Tamanho: quantidade de pares chave e valor
print(len(pessoa))

# Limpando todos os dados do dicionário
copia_pessoa = pessoa.copy()  # cria uma cópia antes de limpar
pessoa.clear()

print(pessoa)        # {}
print(copia_pessoa)  # mantém os dados copiados

#um dicionario aponta somente para um valor, mas esse valor pode possuir diferentes formatos

aluno = {
    "nome": "Julia",
    "notas": [8.5, 7.0, 9.2],  # uma chave com vários valores em uma lista
    "disciplinas": ["Python", "Matemática", "Inglês"]
}

print(aluno["notas"])      # [8.5, 7.0, 9.2]
print(aluno["notas"][0])   # 8.5