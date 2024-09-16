
# total = 0
# for numero in numeros:
#     total += numero

# print(total)

numeros = (2, 5, 6, 7, 9, 23, 27)

def media(*args):
    total = 0
    for i in args:
        total += i
    return total

print(*numeros)
print(media(*numeros))
    