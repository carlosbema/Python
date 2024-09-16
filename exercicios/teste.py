def criar_multiplicador(valor_multiplicador):
    def multiplicador(valor_multiplicado):
        resultado = valor_multiplicador * valor_multiplicado
        return resultado
    return multiplicador

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(8))
print(triplicar(9))
print(quadruplicar(15))