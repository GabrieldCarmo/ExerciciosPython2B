try:
    valor = float(input("Digite o valor do produto: "))
    qtd = int(input("Digite a quantidade de produto: "))
    print(valor * qtd)

except ValueError:
    print("Valor Inválido!")