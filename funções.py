def par_impar(x):
    y = x % 2  
    if y == 0:
        return "par"
    else:
        return "impar"

a = par_impar(4)
print(a)
