salario = float(input("Digite seu salario: "))
cargo = input("Digite seu cargo (Junior, Pleno ou Senior)").capitalize()

if cargo == "Junior":
    novo_salario = salario * 1.10 + 200 if salario <= 1000 else 0
elif cargo == "Pleno":
    novo_salario = salario * 1.15
elif cargo == "Senior":
  filhos = int(input("Quantos filhos você tem? (digite 0 se nao tiver filhos)"))
  novo_salario = salario * 1.20 + filhos * 500
else:
    novo_salario = salario
    print("Cargo não reconhecido. Salário sem aumento.")

print(f"seu novo salario é: R$ {novo_salario:.2f}")    