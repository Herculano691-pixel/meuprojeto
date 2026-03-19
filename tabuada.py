numero = int(input("Digite um número para ver a tabuada: "))

for i in range(101):
    
    resultado = numero * i
    print(f"{numero} {chr(215)} {i} = {resultado}")

    if i % 10 == 0 and i != 0:
        resp = input("Deseja continuar? (s/n): ").lower()
        if resp == "n":
            input("Bye")
            break
   
   #(129399) = 🥷  
   #chr(215) = ×
   
