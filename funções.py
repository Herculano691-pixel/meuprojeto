#para criar função 'def'
def par_impar(x): 
    y = x % 2  
    if y == 0:
        return "par"
    else:
        return "impar"

a = par_impar(4)
print(a)

"""
try:
    y = [1, 2, 3]
    print(y[3])
except:
    print("tem um erro")