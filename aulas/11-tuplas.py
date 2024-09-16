#tuplas funcionam como listas, mas são IMUTÁVEIS e mais eficientes

nomes = ('carlos', 'vinicius', 'boehme')
print(nomes)

nomes = tuple(nomes) #converter listas para tuplas
nomes = list(nomes) #converter tuplas em listas