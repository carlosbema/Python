#utilizando o *args, não é necessário declarar cada variável da
#função definida, a função irá utilizar os argumentos passados
#na chamada

def soma(*args):
    print(args), type(args)
    total = 0
    for numero in args:
        total += numero
        print(numero, total)

soma(1, 2, 3, 4, 5, 6)