#lista.append(x) - adiciona ao final
#lista.insert(i, x) - adiciona no índice escolhido
#lista.pop() ou lista.pop(x) - remove e retorna um índice
#del lista[x] - apaga um índice
#lista.clear() - limpa a lista
#extend - estende a lista
#+ - concatena listas



#lista = [123, True, 'Vinicius', 1.2, []]
#print(lista[3], type(lista[1]))
lista2 = [10, 20, 30, 40, 50]
#lista2[2] = 300
#del lista2[2]
#print(lista2[2])
lista2.append(60)
lista2.pop()
lista2.append(70)
lista2.append(80)
ultimo_valor = lista2.pop()
print(lista2, 'Removido: ', ultimo_valor)

lista3 = [1, 2, 3]
lista4 = [4, 5, 6]
lista5 = (lista3 + lista4)
print(f'Lista3 + Lista4 = {lista5}')
lista6 = lista3.extend(lista4)
print(f'Lista6 = Lista3 extends lista4 = {lista6}')
lista3 = [1, 2, 3]
lista3.extend(lista4)
print(f'lista3 extends lista4 = {lista3}')


