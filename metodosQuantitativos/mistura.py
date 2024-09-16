from pyomo.environ import *

# Criação do modelo
V = 100

A = 0.04

components = {
    'Cerveja A': {'A': 0.045, 'P': 0.32},
    'Cerveja B': {'A': 0.037, 'P': 0.25},
    'Água':      {'A': 0.000, 'P': 0.05},
    #'Vinho':     {'A': 0.083 ,'P': 0.41},
}

c = 'Cerveja B' # Componente
print(components[c]['A']) # Teor alcoólico
print(components[c]['P']) # Preço

# O conjunto de componentes pode ser obtido pelas chaves do dicionário de dados
print(components.keys())

# Lista de componentes
C = components.keys()

# Modelo
model = ConcreteModel()

# Variáveis de decisão: uma para cada componente
model.x = Var(C, domain = NonNegativeReals)

# Função objetivo
model.cost = Objective(expr = sum(model.x[c] * components[c]['P'] for c in C))

# Restrições
model.vol = Constraint(expr = sum(model.x[c] for c in C) == V)
model.alc = Constraint(expr = sum(model.x[c] * components[c]['A'] for c in C) == A * V)

# Solução
solver = SolverFactory('glpk')
solver.solve(model)

print('Mistura ótima')
for c in C:
    print('>', c, ':', model.x[c](), 'litros')
print()
print('Volume =', model.vol(), 'litros')
print('Custo = $', model.cost())