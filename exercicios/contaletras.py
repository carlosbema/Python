frase = 'O Python é uma linguagem de programação '\
        'multiparadigma.'\
        'Python foi criado por Guido van Rossum'
qnt_mais_apareceu = 0
letra_mais_apareceu = ''
i = 0
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1
        continue
    else:
        if frase.count(letra_atual) > qnt_mais_apareceu:
                qnt_mais_apareceu = frase.count(letra_atual)
                letra_mais_apareceu = letra_atual
                i += 1
        else:
                i+=1
                continue
print(f'A letra "{letra_mais_apareceu}" foi a que mais apareceu, \
aparecendo {qnt_mais_apareceu} vezes na frase')

    