def fatorial(a):
    i = a
    total = 1
    while i > 0:
        total *= i
        i -= 1
    return total, a

valor_base = int(input('Digite o número a ser fatorado: '))
print(f'O fatorial de {fatorial(valor_base)[1]} é {fatorial(valor_base)[0]}')