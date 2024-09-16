import os
lista_compras = []
while True:
    print('Selecione uma opção: ')
    operacao = input('[i]nserir [a]pagar [l]istar').lower()
    
    #inserir
    if operacao == 'i':
        os.system('cls')
        produto = input('Insira o produto: ')
        lista_compras.append(produto)
    
    #apagar
    elif operacao == 'a':
        apagar = input('Digite o indice para apagar: ')
        try:
            int_apagar = int(apagar)
            del lista_compras[int_apagar]
        except:
            print('Não foi possível apagar esse índice')

    #listar
    elif operacao == 'l':
        os.system('cls')
        for i, n in enumerate(lista_compras):
            print(i, n)

    #inválido
    else:
        continue

