# nomes = ['carlos', 'vinicius', 'boehme']
# nome1, nome2, nome3 = nomes
# print(nome2)

nome1, *resto = ['carlos', 'vinicius', 'boehme', 'danieli']
print(nome1)

#*resto cria uma nova lista com o que não foi desempacotado