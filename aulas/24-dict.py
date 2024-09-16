pessoa = {
    'nome': 'Luiz Otavio',
    'sobrenome': 'Miranda',
    'idade': '18',
    'altura': '1,8m',
    'endereços': [
        {'rua': 'Carlos Eckelberg', 
         'número': '42'},
        {'rua': 'Osvaldo Schroeder',
         'número:': '80'}
    ],
}

print(pessoa['nome'])
print(pessoa['sobrenome'])

for chave in pessoa:
    print(chave, pessoa[chave])
