cpf = '638667882'
cpf_corrigido = cpf.replace('.', '')[0:9]

digito1 = 0
i = 10
for digito in cpf_corrigido:
    digito1 += int(digito) * i
    i -= 1

digito1 *= 10
digito1 %= 11
print(f'O primeiro digito do CPF é {digito1 if digito1 <= 9 else 0}')