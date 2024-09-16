def saudacao(msg):
    def saudar(nome):
        return f'{msg}, {nome}'
    return saudar

bom_dia = saudacao('Bom dia')
boa_noite = saudacao('Boa noite')

lista_nomes = ['Carlos', 'Vinicius', 'Bernardo']
for nome in lista_nomes:
    print(bom_dia(nome))
    print(boa_noite(nome))