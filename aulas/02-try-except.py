#try = tenta executar o codigo
#except = erro ao tentar executar

numero_str = input('Digite um numero: ')

try:
    numero_f = float(numero_str)
    print(f'O dobro de {numero_f} é {numero_f * 2:.2f}')
except:
    print('Isso não é um número')
    
# if numero_str.isdigit():
#     numero_f = float(numero_str)
#     print(f'O dobro de {numero_f} é {numero_f * 2:.2f}')
# else:
#     print('Isso não é um número')