hora = input('Digite o horario ')

try:
    hora_int = int(hora)
except:
    print('Digite um número inteiro')

manha = hora_int >=0 and hora_int <=11
tarde = hora_int >= 12 and hora_int <= 17
noite =  hora_int >=18 and hora_int <= 23
if manha:
    print('Bom dia')
elif tarde:
    print('Boa tarde')
elif noite:
    print('Boa noite')
else:
    print('A hora digitada é inválida')
