nome = 'Carlos Vinicius' #Iteráveis
tamanho_nome = len(nome)
contador = 0
new_name = ''

while contador < tamanho_nome:
    letra = nome[contador]
    new_name =new_name + '*' + letra
    contador += 1
print(new_name)

