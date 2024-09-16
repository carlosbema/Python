cpf = '6386678826'
cpf_corrigido = cpf.replace('.', '').replace('-', '')[0:10]

digito2 = 0
i = 11
for digito in cpf_corrigido:
    digito2 += int(digito) * i
    i -= 1

digito2 *= 10
digito2 %= 11
print(f'O segundo digito do CPF é {digito2 if digito2 <= 9 else 0}')