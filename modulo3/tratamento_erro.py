# try / except

#o except é basicamente um "se der erro faça isso"

nome = input("Digite o seu nome: ")

try: 
    print(f"Olá {nome}, seja bem vindo(a) ao nosso sistema")

except: 
    print("o código deu erro")


#para melhorar e fazer especificação de um erro
try: 
    print(f"Olá {nome}, seja bem vindo(a) ao nosso sistema")

except Exception as erro: # except Exception(clase exclusiva de python) as erro( a excessão vai ser denominada como erro): 

      print(f"o código deu erro! O erro foi: {erro}") # vai imprimir o erro na tela



# um exemplo de erro com resolução de problema
try:
    idade = int(input("Qual a sua idade?"))   
    nova_idade = idade + 1
    print(f"Sua nova idade é:"(nova_idade))

except Exception as erro:
    print(f"Deu erro: {erro}")
    idade = int(idade) # idade recebe o int apropriado
    nova_idade = idade + 1

