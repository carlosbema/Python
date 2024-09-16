def maiusculas(*args):
    texto_maiusculo = ''
    for letra in args:
        texto_maiusculo += letra
    return texto_maiusculo.upper()

texto = 'Olá, tudo bem?'
print(maiusculas(texto))