#Quando uma lista "copia" uma outra, ela não copia realmente,
#ela aponta para o mesmo lugar na memória, o que faz com que
#qualquer alteração na primeira lista seja refletida na segunda

lista1 = ['Vinicius', 'Dani']
lista2 = lista1

lista1[0] = 'Carlos'
print(lista2)

#Para que uma lista realmente copie a outra sem que haja
#dependencia, deve-se utilizar o método copy

lista3 = ['Bruce', 'Jesus']
lista4 = lista3.copy()

lista3[0] = 'Carioca'
print(lista4)

#Também é possível utilizar for em listas

lista = ['Carlos', 'Vinicius', 'Boehme']

for i in lista:
    print(i)