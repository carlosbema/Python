from pyomo.environ import *

# Dados do problema
V = 100  # Volume do pedido em litros
A_bar = 0.04  # Teor alcoólico desejado (6%)

# Conjunto de componentes
components = ['Cerveja_Forte', 'Cerveja_Fraca', 'Agua']

# Parâmetros
P = {'Cerveja_Forte': 0.32,  # Preço por litro
     'Cerveja_Fraca': 0.25,
     'Agua': 0.05}

A = {'Cerveja_Forte': 0.045,  # Teor alcoólico
     'Cerveja_Fraca': 0.037,
     'Agua': 0.0}

# Criando o modelo
model = ConcreteModel()

# Variáveis de decisão
model.x = Var(components, domain=NonNegativeReals)

# Função objetivo: minimizar o custo total
def objective_rule(model):
    return sum(model.x[c] * P[c] for c in components)
model.cost = Objective(rule=objective_rule, sense=minimize)

# Restrição de volume total
def volume_constraint_rule(model):
    return sum(model.x[c] for c in components) == V
model.volume_constraint = Constraint(rule=volume_constraint_rule)

# Restrição de teor alcoólico
def alcohol_constraint_rule(model):
    return sum(model.x[c] * A[c] for c in components) == A_bar * V
model.alcohol_constraint = Constraint(rule=alcohol_constraint_rule)

# Resolvendo o modelo usando o solver GLPK
solver = SolverFactory('glpk')
result = solver.solve(model)

# Exibindo os resultados
print("Status da Otimização:", result.solver.status)
print("Condição de Término:", result.solver.termination_condition)
print("\nValores Ótimos das Variáveis:")
for c in components:
    print(f"Quantidade de {c}: {model.x[c]():.2f} litros")
    
print(f"\nCusto Total: R$ {model.cost():.2f}")