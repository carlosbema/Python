def cria_multiplicador(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

duplicar = cria_multiplicador(2)
triplicar = cria_multiplicador(3)
quadruplicar = cria_multiplicador(4)

print(duplicar(2))
print(triplicar(3))
print(quadruplicar(4))