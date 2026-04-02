# x = {'a': 1, 'b:' [1, "a", "c"] {}}
# x{"b"} = 999
# print(x)

produtos = {}

while True:
    nome = input("Digite o produto: ")
    valor = float(input("Digite o valor: "))
    produtos[nome] = valor

    print("\nLista de produtos:")
    for produto in produtos:
        print(produto, "- R$ %.2f" % produtos[produto])

    continuar = input("Quer adicionar mais? (s/n): ")

    if continuar == "n":
        break