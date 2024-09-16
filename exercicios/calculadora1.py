while True:
        num1 = input('Digite o primeiro número ')
        operador = input('Digite o operador (+ - * /)')
        num2 = input('Digite o segundo número ')

        numeros_validos = None

        try:
             num1f = float(num1)
             num2f = float(num2)
             numeros_validos = True
        except:
             numeros_validos = None

        if numeros_validos == None:
            print('Um ou ambos os números digitados são inválidos')
            continue
        
        operadores = '+-*/'

        if operador not in operadores:
            print('O operador digitado é inválido')
            continue

        if len(operador) > 1:
            print('Digite apenas 1 operador')
            continue

        if operador == '+':
            print(num1f + num2)
        elif operador == '-':
            print(num1f - num2)
        elif operador == '*':
            print(num1 * num2)
        elif operador == '/':
            print(num1f / num2)
        else:
            print('Não deve chegar aqui') 
        sair = input('Digite S para sair?').lower().startswith('s')
        if sair is True:
            break
