numero = float(input("numero:"))

numero2 = input("numero 2:")

#mostra qual o tipo primitivo do valor
print(type(numero), type(numero2))
print(numero, numero2)

#mostra qual o tipo do valor e realiza a conversão
print(type(int(numero)), type(int(numero2)))
print(numero, numero2)

#com o int na saida do numero ja mostra o valor convertido
print(type(int(numero)), type(numero2))
print(int(numero), numero2)

# faz soma de uma string com um valor inteiro, o que não seria permitido sem a conversão
texto = "500"
print(int(texto)+ 1500)

#substitui o . (natural de numeros float americanos) por virgula
texto_num = "1.777" #valor string
print(float(texto_num) + 100) #transforma string em float para permitir a conta
print((texto_num.replace(".", ",")))