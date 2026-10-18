#inteiros, pontos flutuantes, booleanos, strings
idade = int (input('Digite sua idade:'))
print (idade + 10)

saldo = float(input("Digite o seu saldo"))
#utilizar a f-string permite que o compilador entenda "depois desse f no texto formatado irei colocar entre chaves as variaveis que eu declarei
print(f"O seu saldo é igual a {saldo} mas você precisa de um saldo equivalente a idade de {idade} anos")

# Formatação de nome pode se usar lower para tudo minusculo upper para tudo maiusculo, title para deixar a primeira letra da frase em maiusculo e capitalize para deixar apenas a primeira letra de cada palavra maiusculo

nome =input('Digite o seu nome') 

print(nome.upper(), nome.lower(), nome.title(), nome.capitalize())

