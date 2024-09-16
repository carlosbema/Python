contador = 0
while contador < 10:
    contador += 1
    if contador == 6:
        continue #continua força a volta ao inicio do while
                 #então o 6 não é printado
    print (contador)
    if contador == 40:
        break

print('Acabou')