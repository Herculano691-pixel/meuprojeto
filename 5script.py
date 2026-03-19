# Metodo de repetição while, repetição infinita while true.

#i = 1
#soma = 0

#while i <= 10:
  #  i += 1
   # soma += i

#media = soma / 10
#print(f"A media de 1 a 10 é: {media}")



while True:
    print("estou travado aqui")
    sair = input("Você gostaria de sair? ").lower()
    if sair == "sim":
        print("Bye!")
        break
    elif sair == "não":
        continue
