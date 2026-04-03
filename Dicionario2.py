tabela = {
    "alface": 5.00,
    "tomate": 8.30,
    "limão": 4.45,
    "banana": 5.67
}

total = 0  

while True:
    produto = input("Qual produto deseja comprar? ").lower()
    
    if produto in tabela:
        quantidade = float(input("Quantidade: "))
        total += tabela[produto] * quantidade
    else:
        print("Produto não disponível.")
    
    continuar = input("Deseja adicionar mais produtos? (s/n): ").lower()
    if continuar != "s":
        break

print(f"\nValor total da compra: R$ {total:.2f}")