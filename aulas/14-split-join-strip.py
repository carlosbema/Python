frase1 = '         Teste     Teste, teste,         testes'
#split vai criar uma lista separando a frase nos espaços
#pode separar baseado no argumento em vez dos espaços
lista_palavras = frase1.split(',')

lista_palavras_fixed = []
#strip remove espaço ou caracteres do INICIO ou FIM
for i, frase1 in enumerate(lista_palavras):
    lista_palavras_fixed.append(lista_palavras[i].strip())

# print(lista_palavras)
# print(lista_palavras_fixed)

frases_unidas = ''.join()