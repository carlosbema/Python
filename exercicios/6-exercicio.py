import os
palava_secreta = 'sabonete'
letras_certas = ''
num_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    num_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas letra')
        continue
    if not letra_digitada.isalpha:
        print('Você digitou algo inválido. Digite uma letra: ')
    if letra_digitada in palava_secreta:
        letras_certas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palava_secreta:
        if letra_secreta in letras_certas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)
    
    if palavra_formada == palava_secreta:
        os.system('cls')
        print('Você acertou.')
        print('A palavra era:', palava_secreta)
        print('Tentativas: ', num_tentativas)
        letras_certas = ''
        num_tentativas = 0
 
