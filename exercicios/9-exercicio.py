def mult(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

def par_impar(a):
    resultado = a % 2
    if resultado == 0:
        return f'O número {a} é par'
    return f'O número {a} é impar'

mult1 = mult(3, 5, 10, 6, 8, 15, 20 )
print(mult1)

par_impar1 = par_impar(49)
print(par_impar1)
