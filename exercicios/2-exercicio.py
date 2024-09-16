num = input('Digite um número inteiro')
try:
    num_int = int(num)
    resto = num_int % 2
    if resto == 0:
        print('Número par')
    else:
        print('Número impar')
except:
    print('Não é um número inteiro')
