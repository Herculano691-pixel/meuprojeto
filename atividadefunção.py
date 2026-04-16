def salario_novo(salario, cargo):
    if cargo == 'Junior':
        return salario * 1.05
    if cargo == 'Pleno':
        return salario * 1.10
    if cargo == 'Senior':
        return salario * 1.15
    
    print('Cargo não existe')
    return salario

resultado = salario_novo(1000, 'Senior')
print('Salário novo:', resultado)
