def saudacao(msg):
    def nome(nome):
        return f'{msg}, {nome}'
    return nome

bem_vindo_pessoa = saudacao('Bem vindo')
lista_nomes = ['Vinicius', 'Joao', 'Pedro', 'José']
for nome in lista_nomes:
    print(bem_vindo_pessoa(nome))