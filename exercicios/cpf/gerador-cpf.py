import random
import sys

cpf = ''
for i in range(9):
    cpf += str(random.randint(1, 9))
    i += 1
print(cpf)

cpf_corrigido = cpf.replace('.', '')[0:9]

digito1 = 0
i = 10
for digito in cpf_corrigido:
    digito1 += int(digito) * i
    i -= 1

digito1 *= 10
digito1 %= 11
cpf_corrigido += str(0 if digito1 > 9 else digito1)

digito2 = 0
i = 11
for digito in cpf_corrigido:
    digito2 += int(digito) * i
    i -= 1

digito2 *= 10
digito2 %= 11
cpf_corrigido += str(0 if digito2 > 9 else digito2)

print(cpf_corrigido)

