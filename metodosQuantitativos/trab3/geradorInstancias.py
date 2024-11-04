import random

# Projetos disponíveis
projetos = ['Driblando', 'SMART', 'PlanetHeroes', 'X4CHANGE']

# Gerar 10 trainees aleatórios
trainees = []
for i in range(10):
    trainee = {
        'id': f'T{i+1:02d}',
        'projeto': random.choice(projetos),
        'alergia': random.choice(['Sim', 'Não'])
    }
    trainees.append(trainee)

# Salvar em arquivo txt
with open('trainees.txt', 'w') as f:
    f.write('ID|Projeto|Alergia\n')  # Header
    for t in trainees:
        f.write(f"{t['id']}|{t['projeto']}|{t['alergia']}\n")

print("Arquivo trainees.txt gerado com sucesso!")