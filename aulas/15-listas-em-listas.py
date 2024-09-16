salas = [
    ['Maria', 'Helena'],
    ['Elaine', ],
    ['Luiz', 'Joao', 'Eduarda', 
     (0, 10, 20, 30, 40)
     ]
]

for i, sala in enumerate(salas):
    print(f'Sala: {i + 1}')
    for aluno in sala:
        print(f'Aluno: {aluno}')