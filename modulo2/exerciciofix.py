nome = (input("Digite aqui o nome do produto:"))
preco_uni = (float(input("Digite o preço unitário:")))
quantidade = (int(input("Digite a quantidade:")))

valortotal = preco_uni * quantidade

valordescontado =  0.05 * valortotal

desconto_fixo = valortotal - 0.05 * valortotal

print("------Recibo Fiscal-------")
print(f"Nome do produto: {nome.title}\n Preço Unitário: {preco_uni}\n Quantidade de produto: {quantidade}\n Valor Total: {valortotal:.2f}\n Desconto : -{valordescontado:.2f}\n Valor a ser pago: {desconto_fixo:.2f}")
