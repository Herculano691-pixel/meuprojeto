lista = []

while True:
    n = input("Digite um número (sair para parar): ")
    

    if n == "sair":
        input("Bye")
        break

    lista.append(int(n))
    print(lista)