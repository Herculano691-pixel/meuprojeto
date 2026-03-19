import os
salario = float(input("Qual o seu sálario?"))
percentual = float(input("Qual o percentual de aumento  (%) ?"))
novo_salario = salario * (1 + percentual / 100)

os.system("cls")
print("=" * 30)
print(f"seu salario será de: {novo_salario:.2f}" )
print("=" * 30)