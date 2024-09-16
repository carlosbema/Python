def primo(a):
    if a <= 3:
        return True
    divisor = 2
    while (divisor * divisor) <= a:
        if a % divisor == 0:
            return False
        else:
            divisor += 1 
            continue
    return True
    
numero = int(input('Digite o número para verificar: '))
print(f'{numero} é primo' if primo(numero) is True else f'{numero} não é primo')